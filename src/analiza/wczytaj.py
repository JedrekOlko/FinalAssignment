import pandas as pd
import numpy as np

def wczytaj_formatuj(data_PKB, data_mieszkancy, data_emisjaCO2, from_year, to_year):
    data_PKB.drop('Unnamed: 66', axis=1, inplace=True)
    data_mieszkancy.drop('Unnamed: 66', axis=1, inplace=True)

    # zamienam nazwy krajow we wszystkich danych na pisane tylko duzymi literami
    data_PKB['Country Name'] = data_PKB['Country Name'].str.upper()
    data_mieszkancy['Country Name'] = data_mieszkancy['Country Name'].str.upper()
    data_emisjaCO2['Country'] = data_emisjaCO2['Country'].str.upper()

    # laduje slownik odpowiadajacych sobie krajow w roznych formatach
    with open('saved_dictionary.pkl', 'rb') as f:
        corec_dict = pickle.load(f)

    # ujednolicam format nazw krajow
    data_PKB['Country Name'].replace(corec_dict, inplace=True)
    data_mieszkancy['Country Name'].replace(corec_dict, inplace=True)
    data_emisjaCO2['Country'].replace(corec_dict, inplace=True)

    # zapisuje nazwy unikalnych nazw krajow po ujednoliceniu
    diff_names = (set(data_PKB['Country Name']) | (set(data_mieszkancy['Country Name'])) | (
        set(data_emisjaCO2['Country']))) - \
                 (set(data_PKB['Country Name']) & set(data_mieszkancy['Country Name']) & set(data_emisjaCO2['Country']))

    # pozbywam sie krajow niewystepujacych we wszsytkich 3 zbiorach danych
    data_PKB = data_PKB[~data_PKB['Country Name'].isin(diff_names)]
    data_mieszkancy = data_mieszkancy[~data_mieszkancy['Country Name'].isin(diff_names)]
    data_emisjaCO2 = data_emisjaCO2[~data_emisjaCO2['Country'].isin(diff_names)]

    # tworze zbior lat wystepujacych we wszystkich zbiorach i z przedzialu [from_year, to_year]
    com_years = set(np.arange(from_year, to_year, 1, dtype='int').astype(str)) & set(data_PKB.columns[4:].astype(str)) \
                & set(data_mieszkancy.columns[4:].astype(str)) & set(data_emisjaCO2['Year'].astype(str))

    # licze nowe dataframe, zawierajace tylko wybrane lata
    data_PKB = data_PKB[list(data_PKB.columns[:4]) + sorted(list(com_years))]
    data_mieszkancy = data_mieszkancy[list(data_PKB.columns[:4]) + sorted(list(com_years))]
    data_emisjaCO2 = data_emisjaCO2[data_emisjaCO2['Year'].isin(list(map(int, com_years)))]

    # rozdzielam kolumny dotyczace lat w wiersze w tabelkach pkb i mieszkanyc
    data_PKB = pd.melt(data_PKB, id_vars=data_PKB.columns[:4], var_name='Year', value_name='GDP')
    data_mieszkancy = pd.melt(data_mieszkancy, id_vars=data_mieszkancy.columns[:4], var_name='Year',
                              value_name='Population')

    # scalam wszystkie df w jeden
    data_PKB['Year'] = data_PKB['Year'].astype(int)
    data_mieszkancy['Year'] = data_mieszkancy['Year'].astype(int)
    data_emisjaCO2['Year'] = data_emisjaCO2['Year'].astype(int)

    data_PKB.rename(columns={'Country Name': 'Country'}, inplace=True)
    data_mieszkancy.rename(columns={'Country Name': 'Country'}, inplace=True)

    data_final = pd.merge(data_PKB[['Country', 'Year', 'GDP']], data_mieszkancy[['Country', 'Year', 'Population']])
    data_final = pd.merge(data_final, data_emisjaCO2[['Country', 'Year', 'Total']])
    return (data_final)
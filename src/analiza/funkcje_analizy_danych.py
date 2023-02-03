import pandas as pd
import numpy as np

def CO2_na_mieszkanca(data):
    data_top_CO2 = pd.DataFrame(
        {'Year': data['Year'], 'Country': data['Country'], 'Total Emission': data['Total']
            , 'Average Emission': data['Total'] / data['Population']})
    res = data_top_CO2.groupby(by='Year')['Average Emission'].nlargest(5)
    return( pd.merge(res, data_top_CO2) )
def GDP_na_mieszkanca(data):
    data_top_GDP = pd.DataFrame(
        {'Year': data['Year'], 'Country': data['Country'], 'GDP': data['GDP']
            , 'GDP per capita': data['GDP'] / data['Population']})
    res = data_top_GDP.groupby(by='Year')['GDP per capita'].nlargest(5)
    return( pd.merge(res, data_top_GDP) )

def zmiana_emisji(data):
    ostatnie_lata = sorted(set(data['Year']))[-10:]
    data.dropna(subset=['Total', 'Population'], axis=0, inplace=True)
    data['Average Emission'] = data['Total'] / data['Population']
    data_diff_f = data[data['Year'] == ostatnie_lata[0]].rename(
        columns={'Average Emission': 'Average Emission Start'})
    data_diff_l = data[data['Year'] == ostatnie_lata[-1]].rename(
        columns={'Average Emission': 'Average Emission End'})
    data_diff_f = data_diff_f[data_diff_f['Country'].isin(data_diff_l['Country'])]
    data_diff_l = data_diff_l[data_diff_l['Country'].isin(data_diff_f['Country'])]
    data_diff = pd.merge(data_diff_f.drop(['Year', 'GDP', 'Population', 'Total'], axis=1),
                         data_diff_l.drop(['Year', 'GDP', 'Population', 'Total'], axis=1))
    data_diff['Average Diff'] = data_diff['Average Emission End'] - data_diff['Average Emission Start']
    return(data_diff)


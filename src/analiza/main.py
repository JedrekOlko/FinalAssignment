import argparse
import pandas as pd
import numpy as np
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('gdp', help='path to gdp csv')
parser.add_argument('population', help='path to population csv')
parser.add_argument('CO2emission', help='path to CO2 emission csv')
parser.add_argument('-f', type=int, help='from which year', default=1961)
parser.add_argument('-t', type=int, help='to which year', default=2014)
args = parser.parse_args()

data_PKB = pd.read_csv(args.gdp, skiprows = 4)
data_mieszkancy = pd.read_csv(args.population, skiprows = 3)
data_emisjaCO2 = pd.read_csv(args.CO2emission)
from_year = args.f
to_year = args.t

#zamienam nazwy krajow we wszystkich danych na pisane tylko duzymi literami
data_PKB['Country Name'] = data_PKB['Country Name'].str.upper()
data_mieszkancy['Country Name'] = data_mieszkancy['Country Name'].str.upper()
data_emisjaCO2['Country'] = data_emisjaCO2['Country'].str.upper()

#laduje slownik odpowiadajacych sobie krajow w roznych formatach
with open('saved_dictionary.pkl', 'rb') as f:
    corec_dict = pickle.load(f)

#ujednolicam format nazw krajow
data_PKB['Country Name'].replace(corec_dict, inplace=True)
data_mieszkancy['Country Name'].replace(corec_dict, inplace=True)
data_emisjaCO2['Country'].replace(corec_dict, inplace=True)

#zapisuje nazwy unikalnych nazw krajow po ujednoliceniu
diff_names = (set(data_PKB['Country Name']) | (set(data_mieszkancy['Country Name'])) | (set(data_emisjaCO2['Country'])) ) - \
       (set(data_PKB['Country Name']) & set(data_mieszkancy['Country Name']) & set(data_emisjaCO2['Country']) )

#print( list( sorted(diff_names) ) )
#pozbywam sie krajow niewystepujacych we wszsytkich 3 zbiorach danych
print( data_PKB.shape )
print( data_mieszkancy.shape )
print( data_emisjaCO2.shape )

data_PKB = data_PKB[~data_PKB['Country Name'].isin( diff_names)]
data_mieszkancy = data_mieszkancy[~data_mieszkancy['Country Name'].isin(diff_names)]
data_emisjaCO2 = data_emisjaCO2[~data_emisjaCO2['Country'].isin(diff_names)]


print( data_PKB.shape )
print( data_mieszkancy.shape )
print( data_emisjaCO2.shape )
print( from_year )
print( to_year )
import argparse
import pandas as pd
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('gdp', help='path to gdp csv')
parser.add_argument('population', help='path to population csv')
parser.add_argument('CO2emission', help='path to CO2 emission csv')
parser.add_argument('-f', type = int, help = 'from which year', default=1961)
parser.add_argument('-t', type = int, help = 'to which year', default=2014)
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


diff_pkb_mieszkancy = (set(data_PKB['Country Name']) | (set(data_mieszkancy['Country Name'])) ) - \
       (set(data_PKB['Country Name']) & (set(data_mieszkancy['Country Name']))  )
diff_pkb_CO2 = (set(data_PKB['Country Name']) | (set(data_emisjaCO2['Country'])) ) - \
       (set(data_PKB['Country Name']) & (set(data_emisjaCO2['Country']))  )
with open('saved_dictionary.pkl', 'rb') as f:
    corec_dict = pickle.load(f)
print( corec_dict )




print( data_PKB.head() )
print( data_mieszkancy.head() )
print( data_emisjaCO2.head() )
print( data_PKB.shape )
print( data_mieszkancy.shape )
print( data_emisjaCO2.shape )
print( from_year )
print( to_year )
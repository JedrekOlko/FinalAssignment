import argparse
import pandas as pd

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

print( data_PKB.shape )
print( data_mieszkancy.shape )
print( data_emisjaCO2.shape )
print( from_year )
print( to_year )
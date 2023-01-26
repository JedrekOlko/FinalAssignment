import sys
import pandas as pd
import argparse


path_pkb_c = 'data_files/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv'
path_mieszkancy_c = 'data_files/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv'
path_emisjaCO2_c = 'data_files/data/fossil-fuel-co2-emissions-by-nation_csv.csv'

data_PKB = pd.read_csv(path_pkb_c, skiprows = 4)
data_mieszkancy = pd.read_csv(path_mieszkancy_c, skiprows = 3)
data_emisjaCO2 = pd.read_csv(path_emisjaCO2_c)

print( data_PKB.shape )
print( data_mieszkancy.shape )
print( data_emisjaCO2.shape )

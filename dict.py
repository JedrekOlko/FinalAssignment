import pickle
import pandas as pd

path_pkb_c = 'data_files/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv'
path_mieszkancy_c = 'data_files/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv'
path_emisjaCO2_c = 'data_files/data/fossil-fuel-co2-emissions-by-nation_csv.csv'

data_PKB = pd.read_csv(path_pkb_c, skiprows = 4)
data_mieszkancy = pd.read_csv(path_mieszkancy_c, skiprows = 3)
data_emisjaCO2 = pd.read_csv(path_emisjaCO2_c)

diff_pkb_mieszkancy = (set(data_PKB['Country Name']) | (set(data_mieszkancy['Country Name'])) ) - \
       (set(data_PKB['Country Name']) & (set(data_mieszkancy['Country Name']))  )
diff_pkb_CO2 = (set(data_PKB['Country Name']) | (set(data_emisjaCO2['Country'])) ) - \
       (set(data_PKB['Country Name']) & (set(data_emisjaCO2['Country']))  )

#print( diff_pkb_mieszkancy )
#print( diff_pkb_CO2 )

dict_replace = {
       'ANTIGUA & BARBUDA': 'ANTIGUA AND BARBUDA',
       'BAHAMAS': 'BAHAMAS, THE',
       'BOSNIA & HERZEGOVINA': 'BOSNIA AND HERZEGOVINA',
       'BRUNEI (DARUSSALAM)': 'BRUNEI DARUSSALAM',
       'CABO VERDE': 'CAPE VERDE',
       'CHINA': 'CHINA (MAINLAND)',
       'CONGO': 'CONGO, DEM. REP.',
       'COTE D IVOIRE': "COTE D'IVOIRE",
       'CZECH REPUBLIC': 'CZECHIA',
       'EGYPT': 'EGYPT, ARAB REP.',
       'FAEROE ISLANDS': 'FAROE ISLANDS',
       'FRANCE': 'FRANCE (INCLUDING MONACO)',
       'GAMBIA': 'GAMBIA, THE',
       'GUINEA BISSAU': 'GUINEA-BISSAU',
       'HONG KONG SAR, CHINA': 'HONG KONG SPECIAL ADMINSTRATIVE REGION OF CHINA',
       'IRAN, ISLAMIC REP.': 'ISLAMIC REPUBLIC OF IRAN',
       'ITALY': 'ITALY (INCLUDING SAN MARINO)',
       "KOREA, DEM. PEOPLE'S REP.": 'KOREA, REP.',
       'KYRGYZ REPUBLIC': 'KYRGYZSTAN',
       'LAO PDR': 'LAO PEOPLE S DEMOCRATIC REPUBLIC',
       'MACAO SAR, CHINA': 'MACAU SPECIAL ADMINSTRATIVE REGION OF CHINA',
       'MACEDONIA': 'NORTH MACEDONIA',
       'MYANMAR': 'MYANMAR (FORMERLY BURMA)',
       'SLOVAK REPUBLIC': 'SLOVAKIA',
       'ST. KITTS AND NEVIS': 'ST. KITTS-NEVIS',
       'ST. VINCENT & THE GRENADINES': 'ST. VINCENT AND THE GRENADINES',
       'TURKEY': 'TURKIYE',
       'UNITED STATES': 'UNITED STATES OF AMERICA',
       'VENEZUELA': 'VENEZUELA, RB',
       'VIET NAM': 'VIETNAM',
       'YEMEN': 'YEMEN, REP.'
}

with open('src/analiza/saved_dictionary.pkl', 'wb') as f:
    pickle.dump(dict_replace, f)



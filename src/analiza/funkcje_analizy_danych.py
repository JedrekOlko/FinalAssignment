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
    10_ostatnich_lat = data['Year'].nlargest(10)


from src.analiza.wczytaj import wczytaj_formatuj
from src.analiza.funkcje_analizy_danych import CO2_na_mieszkanca
from src.analiza.funkcje_analizy_danych import GDP_na_mieszkanca
from src.analiza.funkcje_analizy_danych import zmiana_emisji
import pytest
import pandas as pd

p1 = '/home/jedrek/Desktop/Studia/ND/FinalAssignment/data_files/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv'
p2 = '/home/jedrek/Desktop/Studia/ND/FinalAssignment/data_files/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv'
p3 = '/home/jedrek/Desktop/Studia/ND/FinalAssignment/data_files/data/fossil-fuel-co2-emissions-by-nation_csv.csv'

df = wczytaj_formatuj(p1, p2, p3, 1960, 2014)

def test_wczytaj():
    with pytest.raises(TypeError):
        wczytaj_formatuj(p1, p2, p3, 123, '600')
    with pytest.raises(FileNotFoundError):
        wczytaj_formatuj('a', p2, p3, 123, 456)
    with pytest.raises(TypeError):
        wczytaj_formatuj()
def test_wczyaj_out():
    assert isinstance(wczytaj_formatuj(p1, p2, p3, 1960, 2000), pd.DataFrame)

def test_CO2_na_mieszkanca():
    with pytest.raises(TypeError):
        CO2_na_mieszkanca('a')
    with pytest.raises(TypeError):
        CO2_na_mieszkanca()

def test_CO2_na_mieszkanca_out():
    assert isinstance( CO2_na_mieszkanca(df), pd.DataFrame )

def test_GDP_na_mieszkanca():
    with pytest.raises(TypeError):
        GDP_na_mieszkanca('a')
    with pytest.raises(TypeError):
        GDP_na_mieszkanca()

def test_GDP_na_mieszkanca_out():
    assert isinstance( GDP_na_mieszkanca(df), pd.DataFrame )

def test_zmiana_emisji():
    with pytest.raises(TypeError):
        zmiana_emisji('a')
    with pytest.raises(TypeError):
        zmiana_emisji()
    with pytest.raises(TypeError):
        zmiana_emisji(df, 'a')

def test_zmiana_emisji_out():
    assert isinstance( zmiana_emisji(df), pd.DataFrame )
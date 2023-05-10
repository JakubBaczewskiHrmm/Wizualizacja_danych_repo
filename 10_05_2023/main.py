import numpy as np
import pandas as pd
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx,header=0)
#Zad 2
print(df[df['Liczba']>1000])
print(df[(df.Imie == 'JAKUB')])

print('Suma wszystkich urodzonych dzieci w całym okresie' ,df['Liczba'].sum())
print('Suma dzieci urodzonych w latach 2000-2005', df[df['Rok']<2006].sum())
print('suma kobiet i mezczyzn:\n', df.groupby('Plec')['Liczba'].sum())

df_grouped = df.groupby(['Rok','Plec'])['Liczba'].sum()
for year in range(2000,2016):
    najczestsze_k = df[(df['Rok'] == year) & (df['Plec'] == 'K')].nlargest(1,'Liczba')['Imie'].item()
    najczestsze_m = df[(df['Rok'] == year) & (df['Plec'] == 'M')].nlargest(1, 'Liczba')['Imie'].item()
    print(f"Najbardziej popularne imie dziewczynki w {year}: {najczestsze_k}")
    print(f"Najbardziej popularne imie chlopca w {year}: {najczestsze_m}")
najczestsze_k = df[df['Plec'] == 'K'].groupby('Imie')['Liczba'].sum().nlargest(1).index.item()
najczestsze_m = df[df['Plec'] == 'M'].groupby('Imie')['Liczba'].sum().nlargest(1).index.item()
print(najczestsze_k)
print(najczestsze_m)
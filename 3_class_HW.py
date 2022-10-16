"""
1. Pomocí stejného postupu jako výše načti data z Mošnova. 
2. Vytvoř graf, který porovná vývoj ročních úhrnů srážek (tj. vždy suma srážek za daný rok) v jednotlivých stanicích. Dokážeš z grafu vyčíst nějakou zajímavou informaci?
3. Zjisti, ve které z těchto stanic byl nejteplejší den (den s nejvyšší maximální teplotou) v roce 2010 a který den to byl.
"""

# Načtení dat
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def extract_and_clean_chmi_excel_sheet(excel_data, sheet_name):
    """Parse ČHMÚ historical meteo excel data"""
    # načti list z excel souboru a převeď na tidy data formát
    data_tidy = (
        excel_data.parse(sheet_name, skiprows=3)
        .melt(id_vars=["rok", "měsíc"], var_name="den", value_name=sheet_name)
        .dropna()
    )
    # vytvoř časovou řadu datumů
    datum = pd.to_datetime(
        data_tidy[["rok", "měsíc", "den"]].rename(
            columns={"rok": "year", "měsíc": "month", "den": "day"}
        )
    )
    # přidej sloupec datum jako index a odstraň den, měsíc, rok a vrať setříděný výsledek
    return (
        data_tidy.assign(datum=datum)
        .set_index("datum")
        .drop(columns=["rok", "měsíc", "den"])
        .sort_index()
    )
  
# otevři Excel soubor
excel_data_ruzyne = pd.ExcelFile("P1PRUZ01.xls")
# načti všechny listy kromě prvního
extracted_sheets = (
    extract_and_clean_chmi_excel_sheet(excel_data_ruzyne, sheet_name)
    for sheet_name in excel_data_ruzyne.sheet_names[1:]
)
# spoj všechny listy do jednoho DataFrame
ruzyne_tidy = pd.concat(extracted_sheets, axis=1)
ruzyne_tidy

# 1.
MOSNOV_DATA_FILENAME = "O1MOSN01.xls"
# tvuj kod zde
# otevři Excel soubor
MOSNOV_DATA_FILENAME = pd.ExcelFile("O1MOSN01.xls")
# načti všechny listy kromě prvního
extracted_sheets = (
    extract_and_clean_chmi_excel_sheet(MOSNOV_DATA_FILENAME, sheet_name)
    for sheet_name in MOSNOV_DATA_FILENAME.sheet_names[1:]
)
# spoj všechny listy do jednoho DataFrame
MOSNOV_tidy = pd.concat(extracted_sheets, axis=1)
MOSNOV_tidy

# test - show sheets names
# MOSNOV_DATA_FILENAME.sheet_names

# 2.
tvuj kod zde
# 1 mdata/ 2 rdata/ 3 all tab/ 4 graf

#RUZYNE
suma_srazek_R_Y = ruzyne_tidy["úhrn srážek"].resample('Y').sum()
#print(suma_srazek_R_Y.head(5))

#MOSNOV
suma_srazek_M_Y = MOSNOV_tidy["úhrn srážek"].resample('Y').sum()

#oboje
suma_srazek = pd.DataFrame({"suma_srazek_R_Y":suma_srazek_R_Y ,"suma_srazek_M_Y":suma_srazek_M_Y })

suma_srazek.plot(
    y=["suma_srazek_M_Y","suma_srazek_R_Y"],
    figsize=(14,7),
    title = "Porovnani srazek"
);

# v Mosnove je uhrn srazek po vetsinu zkoumaneho obdobi mnohem vyssi, v nekterych letech dosahuje i 2nasobnych hodnot 
# 3.
# tvuj kod zde
# 1 maxim tepl dataframe obou /2 rok 2010/ 3 den?
ruzyne_2010 = ruzyne_tidy.loc[ruzyne_tidy.index.year == 2010]
#print(ruzyne_2010)
tepl_max_R = ruzyne_2010["teplota maximální"].max()

resultR=ruzyne_2010[ruzyne_2010["teplota maximální"]==tepl_max_R]


MOSNOV_2010 = MOSNOV_tidy.loc[ruzyne_tidy.index.year == 2010]
tepl_max_M = MOSNOV_2010["teplota maximální"].max()

resultM=MOSNOV_2010[MOSNOV_2010["teplota maximální"]==tepl_max_M]


if tepl_max_R > tepl_max_M:
    print("Ruzyne\n", resultR["teplota maximální"])
else: 
    print("Mosnov\n",resultM["teplota maximální"])

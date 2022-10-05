"""
1.Vytvoř objekt Series, který bude obsahovat seznam tvých oblíbených filmů a přidej mu index a jméno. Pak přidej kód, který vypíše počet prvků Series.
2.Použij Series vytvořenou v předchozím úkolu a vytvoř DataFrame, která bude obsahovat navíc jméno režiséra či režisérky a rok premiéry.
3.Vytvoř tabulku malé násobilky jako DataFrame (t.j. index i sloupce tvoří čísla 1-10, na průsečících je hodnota součinu).
4.Napiš funkci multiplication_table(n), která vytvoří čtvercovou DataFrame s násobilkou s volitelným počtem řádků a sloupců n.(Stačí jen malinko adaptovat předchozí příklad).
5.Použij tabulku pokémonů z hodiny. Pomocí tzv. indexerů zjisti: jaké hodnoty útoku a obrany má pokémon pikachu?
6.Příště budeme pracovat s tabulkou zemí světa. Stáhni si tabulku jako csv z této adresy a:
-podívej se, jaké obsahuje sloupce
-zkus jí nastavit index podle jména a seřaď řádky podle indexu
-vypiš řádky se zeměmi začínajícími na “Slo” a (subjektivně) je porovnej.
"""

import pandas as pd
# 1.
seznam_filmu = pd.Series(["Holidays", "Rio", "Forrest Gump"],
            name = "film",
            index = ["Film1","Film2","Film3"]
)
seznam_filmu

seznam_filmu.size

# 2.
df_filmy = seznam_filmu.to_frame()

jmeno_rezisera = ["Kevin Smith","Carlos Saldanha","Robert Zemeckis"]
rok_premiery =[2016, 2011, 1993]

df_filmy["reziser"] = jmeno_rezisera
df_filmy["rok"] = rok_premiery
df_filmy

# 3.
table = []
for i in range(1,11):
    #print() 
    radek = []
    for j in range(1,11):
        #print(i*j,end="\t")
        radek.append(i*j)
    table.append(radek)
        
res=pd.DataFrame(table,columns = range(1,11),index=range(1,11))
res

# 4.

def multiplication_table(n):

    '''vytvoří čtvercovou DataFrame s násobilkou s volitelným počtem řádků a sloupců n'''

    table=[]
    for i in range(1,n+1):
        radek = []
        for j in range(1,n+1):
            radek.append(i*j)
        table.append(radek)

    res=pd.DataFrame(table,index=range(1,n+1),columns=range(1,n+1))
    return(res)


multiplication_table(50)

#5.
# import dat
tabulka_pokemonu = pd.read_csv("https://naucse.python.cz/2021/pydata-praha-jaro/pydata/pandas_core/static/pokemon.csv")
pokemoni = tabulka_pokemonu.set_index("name").sort_index()
pokemoni.loc["pikachu", ["attack", "defense"]]

#6.
# import dat
countries = pd.read_csv("https://raw.githubusercontent.com/janpipek/data-pro-pyladies/master/data/countries.csv")
# Podívej se, jaké obsahuje tabulka zemí sloupce
countries.columns
# Zkus jí nastavit index podle jména a seřaď řádky podle indexu
countries_sorted = countries.set_index("name").sort_index()
countries_sorted

# Vypiš řádky se zeměmi začínajícími na “Slo” a (subjektivně) je porovnej.
countries_sorted.loc["Slo":"Slp"]

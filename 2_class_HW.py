"""

1. Podle Keplerových zákonů by pro všechny planety měl být konstantní poměr mezi třetí mocninou velké poloosy elipsy oběžné dráhy a druhou mocninou oběžné doby. Ověř to pomocí načtené tabulky planety.
2. Vytvoř vhodný graf, který velkou poloosu elipsy a oběžnou dobu spojuje
3. Přidej do načtené tabulky countries sloupce women_overweight, men_overweight, kde nadváhou zástupců příslušného pohlaví myslíme průměrné bmi > 25.
4. Zjisti, v jakých zemích, které NEpatří do low_income group, mají průměrně méně než 3000 kalorií na den.
5. Napiš kód, který vytvoří graf bmi mužů a bmi žen v zemích EU. Zkus si pohrát i s parametry - nastav figsize, barvu...

"""

import pandas as pd

# 1
planety = pd.DataFrame({
    "jmeno": ["Merkur", "Venuše", "Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun"],
    "symbol": ["☿", "♀", "⊕", "♂", "♃", "♄", "♅", "♆"],
    "obezna_poloosa": [0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06],
    "obezna_doba": [0.24, 0.62, 1, 1.88, 11.86, 29.46, 84.01, 164.8],
})
planety = planety.set_index("jmeno")    
planety



# tvůj kód zde: 
planety["poloosa**3"] = planety["obezna_poloosa"]**3
planety["doba**2"] = planety["obezna_doba"]**2
planety["pomer"] = planety["poloosa**3"]/planety["doba**2"]
planety["poloosa**3"].round(decimals=2)
planety.round(decimals=2)


# 2

# tvůj kód zde

planety.plot.line(
    x="obezna_poloosa",
    y="obezna_doba",
    title="Graf spojujici velkou poloosu elipsy a oběžnou dobu",
    lw=1,
    style="--",
    marker="*",    
    markersize=5,
    logx=True,
    logy=True);

# 3
# import dat
countries = pd.read_csv("https://raw.githubusercontent.com/janpipek/data-pro-pyladies/master/data/countries.csv")
countries.head()

# tvůj kód zde
women_overweight = countries["bmi_women"] > 25
countries["women_overweight"] = women_overweight

men_overweight = countries["bmi_men"] > 25
countries["men_overweight"] = men_overweight

countries


# 4
# tvůj kód zde
countries1 = countries[(countries["calories_per_day"] < 3000) & (countries["income_groups"] != "low_income")] 
countries1["name"]


# 5
# tvůj kód zde:
eu_countries = countries.set_index("name")
eu_countries = eu_countries.query("is_eu")   
x = eu_countries[["bmi_women", "bmi_men"]].plot.bar(
    figsize=(18, 8),
    ylim=(24.5, 28),               # rozsah osy
    color=["pink", "blue"],       # dvě různé barvy pro dva sloupce
    edgecolor="black",         # střední šeď
    title="Graf bmi mužů a bmi žen v zemích EU"
)




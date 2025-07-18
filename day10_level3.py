# 1. Extraer países que contienen 'land'
from data.countries import countries

land_countries = []
for country in countries:
    if 'land' in country:
        land_countries.append(country)
print("Países que contienen 'land':", land_countries)

# 2. Invertir una lista de frutas usando un bucle
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Frutas en orden inverso:", reversed_fruits)

# 3. Trabajar con countries_data.py
from data.countries_data import countries_data # type: ignore

# Total de idiomas únicos
all_languages = []
for country in countries_data:
    all_languages.extend(country.get('languages', []))
unique_languages = set(all_languages)
print("Total de idiomas únicos:", len(unique_languages))

# Diez idiomas más hablados
from collections import Counter
language_counter = Counter(all_languages)
most_spoken = language_counter.most_common(10)
print("10 idiomas más hablados:", most_spoken)

# 10 países más poblados
populated_countries = sorted(countries_data, key=lambda x: x.get('population', 0), reverse=True)[:10]
top_10_populated = [(country['name'], country['population']) for country in populated_countries]
print("10 países más poblados:", top_10_populated)
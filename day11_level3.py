def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def are_items_unique(lst):
    return len(lst) == len(set(lst))

def are_items_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)

from data.countries import countries_data
from collections import Counter

def most_spoken_languages(n=10):
    all_languages = []
    for country in countries_data:
        all_languages.extend(country.get('languages', []))
    language_counter = Counter(all_languages)
    return language_counter.most_common(n)

def most_populated_countries(n=10):
    sorted_countries = sorted(
        countries_data, key=lambda x: x.get('population', 0), reverse=True
    )
    return [(country['name'], country['population']) for country in sorted_countries[:n]]
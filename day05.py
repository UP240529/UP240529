# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
items = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# 3. Find the length of your list
print(len(items))

# 4. Get the first item, the middle item and the last item of the list
print(items[0])  # first
print(items[len(items)//2])  # middle
print(items[-1])  # last

# 5. Declare a list called mixed_data_types
mixed_data_types = ['Esmeralda', 25, 1.65, 'Single', 'Mexico City']

# 6. Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Intel')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'SAP')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print('Google' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
mid = len(it_companies)//2
if len(it_companies) % 2 == 0:
    print(it_companies[mid-1:mid+1])
else:
    print(it_companies[mid])

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
mid = len(it_companies)//2
if len(it_companies) % 2 == 0:
    del it_companies[mid-1:mid+1]
else:
    del it_companies[mid]
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# Insert Python and SQL after Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# Level 2
# 1. List of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))

# Add min and max again
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# Find median
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print(median)

# Find average
average = sum(ages) / len(ages)
print(average)

# Find range
age_range = max(ages) - min(ages)
print(age_range)

# Compare (min - average) and (max - average)
print(abs(min(ages) - average))
print(abs(max(ages) - average))

# Find the middle country(ies)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid = len(countries)//2
if len(countries) % 2 == 0:
    print(countries[mid-1:mid+1])
else:
    print(countries[mid])

# Divide the countries list into two equal lists
if len(countries) % 2 == 0:
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    first_half = countries[:mid+1]
    second_half = countries[mid+1:]
print(first_half)
print(second_half)

# Unpack the first three countries and the rest as scandic countries
china, russia, usa, *scandic_countries = countries
print(china)
print(russia)
print(usa)
print(scandic_countries)
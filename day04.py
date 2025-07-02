# 1. Concatenate strings
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
result1 = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
print(result1)  # Thirty Days Of Python

str5 = 'Coding'
str6 = 'For'
str7 = 'All'
result2 = str5 + ' ' + str6 + ' ' + str7
print(result2)  # Coding For All

# 2. Declare variable company
company = "Coding For All"

# 3. Print company
print(company)

# 4. Print length of company
print(len(company))

# 5. Uppercase
print(company.upper())

# 6. Lowercase
print(company.lower())

# 7. capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 8. Slice out the first word
print(company[7:])  # For All

# 9. Check if contains 'Coding'
print('Coding' in company)
print(company.index('Coding'))  # or company.find('Coding')

# 10. Replace 'Coding' with 'Python'
print(company.replace('Coding', 'Python'))

# 11. Change 'Python for Everyone' to 'Python for All'
print('Python for Everyone'.replace('Everyone', 'All'))

# 12. Split 'Coding For All'
print(company.split())

# 13. Split companies by comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# 14. Character at index 0
print(company[0])

# 15. Last index
print(len(company) - 1)

# 16. Character at index 10
print(company[10])

# 17. Acronym for 'Python For Everyone'
acronym1 = ''.join([word[0] for word in 'Python For Everyone'.split()])
print(acronym1)

# 18. Acronym for 'Coding For All'
acronym2 = ''.join([word[0] for word in company.split()])
print(acronym2)

# 19. Index of first occurrence of 'C'
print(company.index('C'))

# 20. Index of first occurrence of 'F'
print(company.index('F'))

# 21. rfind last occurrence of 'l' in 'Coding For All People'
print('Coding For All People'.rfind('l'))

# 22. Find first occurrence of 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 23. rindex last occurrence of 'because'
print(sentence.rindex('because'))

# 24. Slice out 'because because because'
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

# 25. Find position of first 'because'
print(sentence.find('because'))

# 26. Slice out 'because because because'
print(sentence[start:end])

# 27. Does 'Coding For All' start with 'Coding'?
print(company.startswith('Coding'))

# 28. Does 'Coding For All' end with 'coding'?
print(company.endswith('coding'))

# 29. Remove trailing spaces
print('   Coding For All      '.strip())

# 30. isidentifier()
print('30DaysOfPython'.isidentifier())  # False
print('thirty_days_of_python'.isidentifier())  # True

# 31. Join libraries with hash and space
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libs))

# 32. New line escape
print("I am enjoying this challenge.\nI just wonder what is next.")

# 33. Tab escape
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 34. String formatting for area
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

# 35. String formatting for arithmetic
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

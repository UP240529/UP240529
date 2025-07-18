person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Verificar si existe la clave 'skills' y mostrar la habilidad del medio
if 'skills' in person:
    skills = person['skills']
    mid = len(skills) // 2
    if len(skills) % 2 == 0:
        print(skills[mid - 1:mid + 1])
    else:
        print(skills[mid])

# Verificar si tiene la habilidad 'Python'
if 'skills' in person:
    print('Python' in person['skills'])

# Determinar
if 'skills' in person:
    skills_set = set(person['skills'])
    if skills_set == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print('He is a fullstack developer')
    else:
        print('unknown title')

# Verificar si está casado y vive en Finlandia
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
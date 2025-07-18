import random

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

def unique_random_numbers():
    return random.sample(range(10), 7)

# Ejemplo de uso:
# print(shuffle_list([1, 2, 3, 4, 5]))
# print(unique_random_numbers())
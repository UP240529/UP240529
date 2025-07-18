def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_empty(param):
    return not bool(param)

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

def calculate_median(lst):
    n = len(lst)
    if n == 0:
        return None
    lst_sorted = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst_sorted[mid - 1] + lst_sorted[mid]) / 2
    else:
        return lst_sorted[mid]

def calculate_mode(lst):
    from collections import Counter
    if not lst:
        return None
    count = Counter(lst)
    max_freq = max(count.values())
    modes = [k for k, v in count.items() if v == max_freq]
    return modes[0] if len(modes) == 1 else modes

def calculate_range(lst):
    return max(lst) - min(lst) if lst else 0

def calculate_variance(lst):
    if not lst:
        return 0
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    import math
    return math.sqrt(calculate_variance(lst))
# 1: Find the Second Largest Distinct Element
def second_largest(t):
    largest = float('-inf')
    second = float('-inf')

    for i in t:
        if i > largest:
            largest = i

    for i in t:
        if i < largest and i > second:
            second = i

    return second

print(second_largest((10, 5, 20, 20, 8, 15)))



# 2: Swap Adjacent Elements
def swap_adjacent(t):
    result = []

    for i in range(0, len(t) -1, 2):
        result.append(t[i+1])
        result.append(t[i])

    return tuple(result)

print(swap_adjacent((1, 2, 3, 4, 5, 6)))



# 3: Most Frequent Element
def most_frequent_tuple(t):
    freq = {}

    for i in t:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    max_count = 0
    most_frequent = None
    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            most_frequent = key

    return most_frequent

print(most_frequent_tuple((1, 2, 2, 3, 1, 2, 4)))
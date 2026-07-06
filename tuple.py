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
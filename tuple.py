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



# 4: Find All Pairs with Target Sum
def find_pairs(t, target):
    seen = set()
    result = set()

    for num in t:
        needed = target - num

        if needed in seen:

            if needed < num:
                pair = (needed, num)
            else:
                pair = (num, needed)

            result.add(pair)

        seen.add(num)

    return result

print(find_pairs((1, 2, 3, 4, 5), 6))



# 5: Longest Consecutive Repetition
def longest_repetition(t):
    if len(t) == 0:
        return 0
    
    current_count = 1
    longest_count = 1

    for i in range(1, len(t)):
        if t[i] == t[i - 1]:
            current_count += 1
        else:
            if current_count > longest_count:
                longest_count = current_count

            current_count = 1

    if current_count > longest_count:
        longest_count = current_count

    return longest_count

print(longest_repetition((1, 1, 2, 2, 2, 3, 3, 1)))



# 6: Group Consecutive Equal Elements
def group_consecutive(t):
    if not t:
        return ()

    result = []
    group = [t[0]]

    for i in range(1, len(t)):
        if t[i] == t[i - 1]:
            group.append(t[i])
        else:
            result.append(tuple(group))
            group = [t[i]]

    result.append(tuple(group))

    return tuple(result)

print(group_consecutive((1, 1, 2, 2, 2, 3, 1, 1)))




# 7: Element with the Largest Gap Between Occurrences
def largest_gap_element(t):
    first_index = {}
    max_gap = -1
    result = None

    for index, value in enumerate(t):
        if value not in first_index:
            first_index[value] = index
        else:
            gap = index - first_index[value]

            if gap > max_gap:
                max_gap = gap
                result = value

    return result


print(largest_gap_element((1, 2, 3, 1, 4, 2, 5, 1)))



# 8: Most Frequent Consecutive Pair
def most_frequent_consecutive_pair(t):
    freq = {}

    for i in range(len(t) - 1):
        pair = (t[i], t[i + 1])

        if pair in freq:
            freq[pair] += 1
        else:
            freq[pair] = 1

    max_count = 0
    result = None

    for pair in freq:
        if freq[pair] > max_count:
            max_count = freq[pair]
            result = pair

    return result


print(most_frequent_consecutive_pair((1, 2, 1, 2, 3, 1, 2)))



# 9: Longest Alternating Parity Streak
def longest_alternating_parity(t):
    if len(t) == 0:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(t)):
        if (t[i] % 2) != (t[i - 1] % 2):
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest


print(longest_alternating_parity(
    (1, 2, 3, 4, 6, 7, 8)
))



# 10: Longest Increasing Consecutive Run
def longest_increasing_run(t):
    if not t:
        return ()

    start = 0
    best_start = 0
    best_length = 1
    current_length = 1

    for i in range(1, len(t)):
        if t[i] > t[i - 1]:
            current_length += 1
        else:
            if current_length > best_length:
                best_length = current_length
                best_start = start

            start = i
            current_length = 1

    if current_length > best_length:
        best_length = current_length
        best_start = start

    return t[best_start:best_start + best_length]


print(longest_increasing_run(
    (5, 1, 2, 3, 0, 4, 5, 6, 7, 2)
))
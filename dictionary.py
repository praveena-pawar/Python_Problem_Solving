# 1: Count Frequency of Elements
def count_frequency(nums):
    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq

print(count_frequency([1, 2, 2, 3, 1, 2]))



# 2: Find the Most Frequent Element
def most_frequent(nums):
    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    highest_freq = 0
    most_frequent_element = None
    for key in freq:
        if freq[key] > highest_freq:
            highest_freq = freq[key]
            most_frequent_element = key

    return most_frequent_element

print(most_frequent([1, 2, 2, 3, 1, 2]))



# 3: Find All Duplicate Elements
def find_duplicates(nums):
    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    uniq = []
    for key in freq:
        if freq[key] > 1:
            uniq.append(key)

    return uniq

print(find_duplicates([1, 2, 2, 3, 1, 4, 5, 5]))



# 4: Find the Least Frequent Element
def least_frequent(nums):
    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    lowest_freq = float('inf')
    least_frequent_element = None
    for key in freq:
        if freq[key] < lowest_freq:
            lowest_freq = freq[key]
            least_frequent_element = key

    return least_frequent_element


print(least_frequent([1, 2, 2, 3, 1, 2]))



# 5: Invert a Dictionary
def invert_dict(d):
    result = {}

    for key in d:
        result[d[key]] = key

    return result

print(invert_dict({"a": 1, "b": 2, "c": 3}))



# 6: Merge Two Dictionaries
def merge_dicts(d1, d2):
    result = {}

    for key in d1:
        result[key] = d1[key]

    for key in d2:
        result[key] = d2[key]

    return result

print(merge_dicts(
    {"a": 1, "b": 2},
    {"b": 20, "c": 3}
))
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


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
print(merge_dicts({"a": 1, "b": 2}, {"c": 3, "d": 4}))



# 7: Count Unique Values
def unique_value_count(d):
    unique = []

    for value in d.values():
        if value not in unique:
            unique.append(value)

    return len(unique)


print(unique_value_count({
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3
}))



# 8: Group Keys by Value
def group_keys_by_value(d):
    result = {}

    for key, value in d.items():
        if value in result:
            result[value].append(key)
        
        else:
            result[value] = [key]

    return result
        
print(group_keys_by_value({
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 2
}))



# 9: Count Characters in a String
def char_frequency(text):
    freq = {}
    
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq

print(char_frequency("banana"))



# 10: Find the First Non-Repeating Character
def first_non_repeating(text):
    freq = {}
    
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in text:
        if freq[ch] == 1:
            return ch

    return None

print(first_non_repeating("aabbcdde"))



# 11: Merge Frequencies of Two Lists
def merge_frequencies(list1, list2):
    freq = {}

    for i in list1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i in list2:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq

print(merge_frequencies(
    [1, 2, 2],
    [2, 3, 1]
))



# 12: Are Two Strings Anagrams
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq = {}
    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    freque = {}

    for ch in s2:
        if ch in freque:
            freque[ch] += 1
        else:
            freque[ch] = 1

    if freq == freque:
        return True

    return False

print(are_anagrams("hello", "world"))
print(are_anagrams("listen", "silent"))



# 13: Find Common Keys
def common_keys(d1, d2):
    result = []

    for i in d1:
        if i in d2:
            result.append(i)

    return result

print(common_keys(
    {"a": 1, "b": 2, "c": 3},
    {"b": 20, "c": 30, "d": 40}
))



# 14: Count Keys with Even Values
def count_even_values(d):
    count_even = 0

    for i in d.values():
        if i % 2 == 0:
            count_even += 1

    return count_even

print(count_even_values({
    "a": 1,
    "b": 2,
    "c": 4,
    "d": 5
}))



# 15: Find the Key with the Maximum Value
def key_with_max_value(d):
    max_value = float('-inf')
    max_key = None

    for key in d.keys():
        if d[key] > max_value:
            max_value = d[key]
            max_key = key

    return max_key

print(key_with_max_value({
    "a": 10,
    "b": 25,
    "c": 15
}))



# 16: Remove Keys with a Given Value
def remove_value(d, target):
    result = {}

    for key, value in d.items():
        if value != target:
            result[key] = value

    return result

print(remove_value(
    {"a": 1, "b": 2, "c": 1, "d": 3},
    1
))



# 17: Find Keys with a Given Value
def find_keys_by_value(d, target):
    result = []

    for key, value in d.items():
        if value == target:
            result.append(key)

    return result

print(find_keys_by_value(
    {"a": 1, "b": 2, "c": 1, "d": 3},
    1
))



# 18: Swap Keys and Values with Duplicate Values
def invert_with_duplicates(d):
    result = {}

    for key, value in d.items():
        if value not in result:
            result[value] = [key]
        else:  
            result[value].append(key)

    return result

print(invert_with_duplicates({
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 2,
    "e": 3
}))



# 19: Sum of All Dictionary Values
def sum_values(d):
    total = 0

    for value in d.values():
        total += value

    return total

print(sum_values({
    "a": 10,
    "b": 20,
    "c": 30
}))



# 20: Count Keys That Start with a Given Letter
def count_keys_starting_with(d, letter):
    count_string = 0

    for key in d.keys():
        if key[0] == letter:
            count_string += 1

    return count_string

print(count_keys_starting_with(
    {
        "apple": 1,
        "ant": 2,
        "ball": 3,
        "banana": 4
    },
    "a"
))



# 21: Count Values Greater Than a Target
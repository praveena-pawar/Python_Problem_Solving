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
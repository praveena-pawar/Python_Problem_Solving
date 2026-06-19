# 1: Sum of All Elements
def list_sum(nums):
    total = 0

    for i in nums:
        total = i + total

    return total


print(list_sum([10, 20, 30, 40]))



# 2: Find the Smallest Element
def find_smallest(nums):
    small_element = nums[0]

    for i in nums:
        if i < small_element:
            small_element = i

    return small_element


print(find_smallest([8, 3, 12, 1, 5]))
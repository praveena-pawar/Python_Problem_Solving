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



# 3: Count Even Numbers
def count_even(nums):
    even_count = 0

    for i in nums:
        if i % 2 == 0:
            even_count += 1

    return even_count

print(count_even([1, 2, 3, 4, 5, 6]))



# 4: Create a List of Squares
def squares_list(nums):
    squares = []

    for i in nums:
        squares.append(i * i)

    return squares

print(squares_list([1, 2, 3, 4]))



# 5: Reverse a List (Without reverse())
def reverse_list(nums):
    reversed_list = []

    for i in range(len(nums)-1, -1, -1):
        reversed_list.append(nums[i])

    return reversed_list


print(reverse_list([1, 2, 3, 4]))



# 6: Find the Index of an Element
def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        
    return -1

print(find_index([10, 20, 30, 40], 30))
print(find_index([10, 20, 30, 40], 50))



# 7: Count Occurrences of a Target
def count_occurrences(nums, target):
    occurrences_count = 0

    for i in nums:
        if i == target:
            occurrences_count += 1

    return occurrences_count

print(count_occurrences([1, 2, 2, 3, 2, 4], 2))



# 8: Remove All Occurrences of a Target
def remove_target(nums, target):
    target_removed = []

    for i in nums:
        if i != target:
            target_removed.append(i)

    return target_removed

print(remove_target([1, 2, 2, 3, 2, 4], 2))



# 9: Find the Second Smallest Element
def second_smallest(nums):
    smallest = nums[0]

    for i in nums:
        if i < smallest:
            smallest = i

    second_small = float('inf')
    for i in nums:
        if i > smallest and i < second_small:
            second_small = i

    return second_small

print(second_smallest([8, 3, 12, 1, 5]))



# 10: Merge Two Lists
def merge_lists(a, b):
    result = []

    for i in a:
        result.append(i)

    for j in b:
        result.append(j)

    return result
    

print(merge_lists([1, 2, 3], [4, 5, 6]))



# 11: Find the Largest Odd Number
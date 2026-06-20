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
def largest_odd(nums):
    large_odd = None

    for i in nums:
        if i % 2 != 0:
            if large_odd is None or i > large_odd:
                large_odd = i

    return large_odd

print(largest_odd([8, 3, 12, 7, 5]))
print(largest_odd([2, 4, 6, 8]))



# 12: Find Common Elements
def common_elements(a, b):
    common_number = []

    for i in a:
        if i in b and i not in common_number:
            common_number.append(i)

    return common_number

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print(common_elements([1, 2, 2, 3], [2, 3, 3, 4]))



# 13: Remove Duplicates from a List
def remove_duplicates(nums):
    unique = []

    for i in nums:
        if i not in unique:
            unique.append(i)
    
    return unique


print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))



# 14: Move All Zeros to the End
def move_zeros(nums):
    non_zeros = []
    zero_count = 0

    for i in nums:
        if i == 0:
            zero_count += 1
        else:
            non_zeros.append(i)
    
    for _ in range(zero_count):
        non_zeros.append(0)  
    
    return non_zeros

print(move_zeros([0, 1, 0, 3, 12]))



# 15: Rotate List Right by One Position
def rotate_right(nums):
    rotated_right = [nums[-1]]

    for i in range(len(nums)-1):
        rotated_right.append(nums[i])

    return rotated_right

print(rotate_right([1, 2, 3, 4, 5]))
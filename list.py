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
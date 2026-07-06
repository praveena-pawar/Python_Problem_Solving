# 1: Remove Duplicates
def remove_duplicates(nums):
    unique_num = set()

    for i in nums:
            unique_num.add(i)

    return unique_num

print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))



# 2: Check if a List Has Duplicates
def has_duplicates(nums):
    unique_num = set()

    for i in nums:
        if i in unique_num:
            return True  
        else:
            unique_num.add(i)  

    return False
      
print(has_duplicates([1, 2, 3, 2]))



# 3: Find Common Elements
def common_elements(a, b):
    common_elements = set()

    for i in (a):
        if i in b:
            common_elements.add(i)

    return common_elements
     
print(common_elements(
    [1, 2, 3, 4],
    [3, 4, 5, 6]
))



# 4: Find Elements Only in the First List
def only_in_first(a, b):
    result = set()

    for i in a:
        if i not in b:
            result.add(i)

    return result

print(only_in_first(
    [1, 2, 3, 4],
    [3, 4, 5, 6]
))



# 5: Elements in Either List, but Not Both
def uncommon_elements(a, b):
    result = set()

    for i in a:
        if i not in b:
            result.add(i)

    for i in b:
        if i not in a:
            result.add(i)

    return result

print(uncommon_elements(
    [1, 2, 3, 4],
    [3, 4, 5, 6]
))



# 6: Check if One Collection Is a Subset
def is_subset(a, b):
    set_b = set(b)

    for item in a:
        if item not in set_b:
            return False

    return True

print(is_subset(
    [1, 2, 3],
    [1, 2, 3, 4, 5]
))



# 7: First Repeated Element
def first_repeated(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)
        
    return None

print(first_repeated([4, 2, 7, 2, 4, 8]))



# 8: Find Missing Numbers in a Range
def missing_numbers(nums, n):
    result = set(nums)
    missing_num = set()

    for i in range(1, n+1):
        if i not in result:
            missing_num.add(i)

    return missing_num

print(missing_numbers([1, 2, 4, 6], 6))



# 9: Count Distinct Elements Across Two Lists
def count_distinct(a, b):
    result = set(b)

    for i in a:
        result.add(i)

    return len(result)


print(count_distinct(
    [1, 2, 2, 3],
    [3, 4, 5, 5]
))



# 10: Check if Two Lists Are Disjoint
def are_disjoint(a, b):
    result = set(b)

    for i in a:
        if i in result:
            return False
    
    return True

print(are_disjoint(
    [1, 2, 3],
    [4, 5, 6]
))
print(are_disjoint(
    [1, 2, 3],
    [3, 4, 5]
))



# 11: Find Elements Appearing in Exactly Two Lists
def elements_in_exactly_two(a, b, c):
    result = set()

    set_a = set(a)
    set_b = set(b)
    set_c = set(c)


    for i in set_a:
        if i in set_b and i not in set_c:
            result.add(i)

    for i in set_a:
        if i in set_c and i not in set_b:
            result.add(i)


    for i in set_b:
        if i in set_c and i not in set_a:
            result.add(i)

    return result

print(elements_in_exactly_two(
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
))



# 12: First Unique Element 
def first_unique(nums):
    seen_once = set()
    seen_multiple = set()

    for i in nums:
        if i not in seen_once and i not in seen_multiple:
            seen_once.add(i)

        elif i in seen_once:
            seen_once.remove(i)
            seen_multiple.add(i)

    for i in nums:
        if i in seen_once:
            return i

    return None

print(first_unique([4, 2, 4, 3, 2, 5]))



# 13: Common Duplicates
def common_duplicates(a, b):
    seen_a = set()
    duplicates_a = set()

    for i in a:
        if i in seen_a:
            duplicates_a.add(i)
        else:
            seen_a.add(i)

    seen_b = set()
    duplicates_b = set()

    for i in b:
        if i in seen_b:
            duplicates_b.add(i)
        else:
            seen_b.add(i)

    result = set()

    for i in duplicates_a:
        if i in duplicates_b:
            result.add(i)

    return result

print(common_duplicates(
    [1, 2, 2, 3, 3, 4],
    [2, 2, 3, 4, 4, 5]
))



# 14: Unique Elements from Each List
def unique_to_each_list(a, b):
    unique_a = set(a)
    unique_b = set(b)

    result_a = set()
    result_b = set()
 

    for i in unique_a:
        if i not in unique_b:
            result_a.add(i)

    for i in unique_b:
        if i not in unique_a:
            result_b.add(i)

    return result_a, result_b

print(unique_to_each_list(
    [1, 2, 3, 4],
    [3, 4, 5, 6]
))

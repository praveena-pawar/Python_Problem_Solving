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
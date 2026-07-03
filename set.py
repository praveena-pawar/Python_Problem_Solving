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
# 1: Remove Duplicates
def remove_duplicates(nums):
    unique_num = set()

    for i in nums:
            unique_num.add(i)

    return unique_num

print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))
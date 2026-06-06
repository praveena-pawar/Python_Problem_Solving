# 1: Write a function count_characters(s) that returns the total number of characters in a string without using len().
def count_characters(word):
    total = 0

    for ch in word:
        total += 1

    return total
print(count_characters("python"))
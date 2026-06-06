# 1: Write a function count_characters(s) that returns the total number of characters in a string without using len().
def count_characters(word):
    total = 0

    for ch in word:
        total += 1

    return total
print(count_characters("python"))



# 2: Write a function count_uppercase(s) that returns the number of uppercase letters in a string.
def count_uppercase(word):
    total = 0

    for ch in word:
        if ch.isupper():
            total += 1

    return total

print(count_uppercase("PyThOn"))
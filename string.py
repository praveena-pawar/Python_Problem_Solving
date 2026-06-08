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



# 3: Write a function count_words(sentence) that returns the number of words in a sentence.
def count_words(words):
    total_words = 0

    for word in words.split():
        total_words += 1

    return total_words

print(count_words("I love Python"))



# 4: Write a function reverse_each_word(sentence) that reverses each word individually while keeping the word order the same.
def reverse_each_word(sentence):
    words = sentence.split()
    reversed_sentence = []

    for word in words:
        reversed_word = ""

        for ch in range(len(word) - 1, -1, -1):
            reversed_word += word[ch]

        reversed_sentence.append(reversed_word)

    return " ".join(reversed_sentence)

print(reverse_each_word("I love Python"))




# 5: Write a function first_non_repeating(s) that returns the first character that appears only once in the string.
def first_non_repeating(word):
    freq = {}

    for ch in word:
        if ch in freq:
            freq[ch] += 1

        else:
            freq[ch] = 1

    for ch in word:
        if freq[ch] == 1:
            return ch


    return None

print(first_non_repeating("aabbcdde"))



# 6: Write a function remove_duplicates(s) that returns a new string with duplicate characters removed while preserving the original order.
def remove_duplicates(word):
    unique = ""

    for ch in word:
        if ch not in unique:
            unique += ch

    return unique

print(remove_duplicates("programming"))



# 7: Write a function max_frequency_char(s) that returns the character that appears the most times in a string.
def max_frequency_char(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1

        else:
            freq[ch] = 1

    max_freq = 0
    max_char = ""
    for ch in s:
        if freq[ch] > max_freq:
            max_freq = freq[ch]
            max_char = ch
           
    return max_char

print(max_frequency_char("banana"))



# 8: Check if Two Strings Are Rotations
 

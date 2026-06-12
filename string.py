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
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    double = s1 + s1

    if s2 in double:
        return True
    else:
        return False
    
print(is_rotation("abcd", "cdab")) 
print(is_rotation("abcd", "acbd"))  



# 9: Write a function longest_word(sentence) that returns the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word("I love learning Python"))



# 10: Write a function compress_string(s) that compresses repeated consecutive characters.
def compress_string(s):
    compressed = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1

    compressed += s[-1] + str(count)

    return compressed

print(compress_string("aaabbcccc"))



# 11: Check if a String Contains Only Digits
def only_digits(s):
   
    for ch in s:
        if not ch.isdigit():
            return False
    
    return True
        
print(only_digits("12345"))  
print(only_digits("12a45"))  



# 12: Capitalize First Letter of Each Word
def capitalize_words(sentence):
    words = sentence.split()
    result = ""

    for word in words:
        capitalized = word[0].upper() + word[1:]
        result += capitalized + " "

    return result.strip()

print(capitalize_words("i love python"))



# 13: Find the Most Frequent Word
def most_frequent_word(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1

        else:
            freq[word] = 1

    max_freq = 0
    most_freq = ""
    for word in words:
        if freq[word] > max_freq:
            max_freq = freq[word]
            most_freq = word
    
    return most_freq

print(most_frequent_word("apple banana apple orange banana apple"))



# 14: Check if a String Is a Pangram
def is_pangram(sentence):
    unique = set()

    for ch in sentence.lower():
        if ch.isalpha():
            unique.add(ch)

    return len(unique) == 26

print(is_pangram("The quick brown fox jumps over the lazy dog"))



# 15: Reverse the Order of Words
def reverse_word_order(sentence):
    words = sentence.split()
    reve = ""

    for word in range(len(words) -1, -1, -1):
        reve +=  words[word] + " "

    return reve.strip()
    

print(reverse_word_order("I love Python"))



# 16: Find All Duplicate Characters

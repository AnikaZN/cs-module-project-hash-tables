# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import os
import re
import string

ordered = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
           'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

with open("ciphertext.txt") as f:
    text = f.read()

def crack_caesar(text):
    counts = {}

    words2 = []

    for char in text:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    count_list = list(counts.items())
    count_list.sort(key=lambda x: -x[1])

    mapping = {}

    for x in range(26):
        mapping[count_list[x][0]] = ordered[x]

    new_text = []

    for char in text:
        if char.isalpha():
            if char in mapping:
                new_text.append(mapping[char])
        else:
            new_text.append(char)

    return "".join(new_text)


print(crack_caesar(text))

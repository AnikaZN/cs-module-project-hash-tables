# Your code here
import os
import re
import string

with open("robin.txt") as f:
    text = f.read()

def hist_words(text_doc):
    counts = {}

    remove = string.punctuation
    remove = remove.replace("'", "") # don't remove apostrophes
    pattern = r"[{}]".format(remove) # create the pattern
    no_punctuation = re.sub(pattern, " ", text_doc)
    words = no_punctuation.split()

    words2 = []

    for word in words:
        word = word.lower()
        words2.append(word)

    for x in words2:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    count_list = list(counts.items())
    count_list.sort(key=lambda x: (-x[1], x[0]))

    width = max([len(word[0]) for word in count_list]) + 2

    for tuple in count_list:
        bar = []
        bar.append(tuple[0])
        for x in range(tuple[1]):
            bar.append('#')
        print(f'{bar[0].ljust(width)}{"".join(bar[1:])}')


print(hist_words(text))

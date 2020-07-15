import re
import string

def word_count(s):
    # Your code here
    counts = {}

    remove = string.punctuation
    remove = remove.replace("'", "") # don't remove apostrophes
    pattern = r"[{}]".format(remove) # create the pattern
    no_punctuation = re.sub(pattern, " ", s)
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

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

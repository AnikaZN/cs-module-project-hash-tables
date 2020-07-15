import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split()

# TODO: analyze which words can follow other words
cache = {}

for x in range(len(words) - 1):
    if words[x] not in cache:
        cache[words[x]] = []
        cache[words[x]].append(words[x + 1])
    else:
        cache[words[x]].append(words[x + 1])

# TODO: construct 5 random sentences
punctuation = ['.', '?', '!']
start = set()
stop = set()

for word in words:
    if word[0] == '"' and word[1].isupper() or word[0].isupper():
        start.add(word)
    if word[-1] == '"' and word[-2] in punctuation or word[-1] in punctuation:
        stop.add(word)
    else:
        pass

def sentence_builder():
    sentence = []

    start_word = random.sample(set(start), 1)[0]
    sentence.append(start_word)

    while sentence[-1] not in stop:
        key = sentence[-1]
        next_word = random.choice(cache[key])
        sentence.append(next_word)
    else:
        return " ".join(sentence)

print(sentence_builder())
print(sentence_builder())
print(sentence_builder())
print(sentence_builder())
print(sentence_builder())

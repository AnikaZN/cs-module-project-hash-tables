"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
q2 = []

for number in q:
    true = f(number)
    q2.append(true)

cache = {}
counter = [x for x in len(q2)]

for x in range(len(q2) - 1):
        cache[((q2[x]) + (q2[x + 1]))] = (q[x], q[x + 1])

print(cache)


## Stuck

import itertools
from itertools import repeat

a = set()
for i in itertools.product('СЛОН', repeat = 5):
    if 1 <= i.count("О") <= 3:
        a.add(i)
print(len(a))
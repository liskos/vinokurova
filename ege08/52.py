import itertools
from itertools import repeat

a = set()
for i in itertools.product('КОМАР', repeat = 4):
    if 0 <= i.count("А") <= 3:
        a.add(i)
print(len(a))
import itertools
from itertools import repeat

a = set()
for i in itertools.product('МУХА', repeat = 5):
    if i.count("У") <= 3:
        a.add(i)
print(len(a))
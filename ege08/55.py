import itertools
from itertools import repeat

a = set()
for i in itertools.product('ЖИРАФ', repeat = 6):
    if 1 <= i.count("А") <= 4:
        a.add(i)
print(len(a))
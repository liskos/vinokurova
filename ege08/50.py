import itertools
from itertools import repeat

a = set()
for i in itertools.product('КАТЕР', repeat = 4):
    if i.count("Р")>= 2:
        a.add(i)
print(len(a))
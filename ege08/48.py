import itertools
from itertools import repeat

a = set()
for i in itertools.product('БАЛКОН', repeat = 5):
    if i.count("Б")>= 1:
        a.add(i)
print(len(a))
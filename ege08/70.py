import itertools
from itertools import repeat

a = set()
for i in itertools.product("АБВГ", repeat = 5):
    if i.count('Г') <= 1 and "Г" in i[:-1]:
        a.add(i)
print(len(a))
        
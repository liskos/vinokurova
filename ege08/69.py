import itertools
from itertools import repeat

a = set()
for i in itertools.product("АБВГДЕ", repeat=4):
    if i.count('Г') == 1 and "Г" in i[0] or "Г" in i[-1]:
        a.add(i)
print(len(a))

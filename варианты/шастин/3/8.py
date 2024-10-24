import itertools
from itertools import repeat

a = set()
for i, s in enumerate(itertools.product("ЕЛОПРСТ", repeat = 5), 1):
    if i % 2  == 1 and s[-1] in "ЕО" and s.count("Е") + s.count("О") >= 2:
        a.add(s)
print(len(a))


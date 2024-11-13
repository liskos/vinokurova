import itertools
from itertools import repeat

a = set()
for i in itertools.product('СИРОП', repeat = 5):
    if i.count("О") == 1 and "СО" in i:
        a.add(i)
    elif i.count("О") == 1 and "РО" in i:
        a.add(i)
    elif i.count("О") == 1 and "ПО" in i:
        a.add(i)
print(len(a))
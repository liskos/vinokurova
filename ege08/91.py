import itertools
from itertools import repeat

a = set()
for i in itertools.permutations("КАЛИЙ", r = 5):
    ss = "".join(i).replace("ИА", "X")
    if i[0] != "Й" and ss.count("X") == 0:
        a.add(i)
        print(i)
print(len(a))
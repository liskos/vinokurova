import itertools
from itertools import repeat

a = set()
for s in itertools.permutations("КРОЙ", r = 4):
    ss = ''.join(s).replace("ОЙ", "X")
    if "Й" not in s[0] and ss.count("X") == 0:
        a.add(s)
        print(s)
print(len(a))
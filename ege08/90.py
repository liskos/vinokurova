import itertools
from itertools import repeat

a = set()
for s in itertools.product("КРОЙ", repeat = 4):
    ss = ''.join(s).replace("ОЙ", "X")
    if s.count("К") == 1 and s.count("Р") == 1 and s.count("О") == 1 and s.count("Й") == 1 and "Й" not in s[0] and s.count("X") == 0:
        a.add(s)
        print(s)
print(len(a))

import itertools
from itertools import repeat

a = set()
for i in itertools.product("ваяющий", repeat=4):
    s = "".join(i)
    if i[0] != "й" and (i.count("а") != 0 or i.count("и") != 0 or i.count("я") != 0 or i.count("ю") != 0):
        a.add(i)
        print(i)
print(len(a))
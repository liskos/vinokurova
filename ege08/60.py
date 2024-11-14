import itertools
from itertools import repeat
k = 0
for i in itertools.product("АБВГЭЮЯ", repeat=5):
    if set(i[1:-1]) <= {'А', "Б", "В","Г"} and i[0] in "ЭЮЯ" and i[-1] in "ЭЮЯ":
        k += 1
print(k)
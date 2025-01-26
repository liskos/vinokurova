import itertools
from itertools import repeat

k = 1
for i in itertools.product("авийкпс", repeat =6):
    s = "".join(i)
    ss = s.replace("и", "а")
    if "аа" in ss:
        k += 1
        if ss == "какааа":
            print(k, i)

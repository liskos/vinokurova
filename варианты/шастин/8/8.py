import itertools
from itertools import repeat
k = set()
for i in itertools.permutations("парижанка"):
    s = "".join(i)
    ss = s.replace("и","а")
    if ss.count("аа") == 1 and ss.count("ааа") == 0:
        k.add(i)
print(len(k))

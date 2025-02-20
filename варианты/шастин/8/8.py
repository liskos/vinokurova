import itertools
from itertools import repeat
k = 0
for i in itertools.permutations("парижанка"):
    s = "".join(i)
    ss = s.replace("и","а")
    if "аа" not in ss:
        k += 1
print(k)

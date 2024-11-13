import itertools
from itertools import repeat
from os import replace

for i, s in enumerate(itertools.product('АДР', repeat = 6), 1):
    if s[0] == "Р":
        print(i, s)
        break
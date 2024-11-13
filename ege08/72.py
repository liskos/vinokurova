import itertools
from itertools import repeat
from os import replace

for i, s in enumerate(itertools.product('АКЛОШ', repeat = 4), 1):
    if s[0] == "О":
        print(i, s)
        break
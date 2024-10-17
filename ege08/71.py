import itertools
from itertools import repeat
from os import replace

for i, s in enumerate(itertools.product('ЕИКНУЧ', repeat = 3), 1):
    if s[0] == "К":
        print(i, s)
        break
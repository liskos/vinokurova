import itertools
from itertools import repeat
from os import replace

for i, s in enumerate(itertools.product('АРТФ', repeat = 5), 1):
    if s[0] == "Т":
        print(i, s)
        break
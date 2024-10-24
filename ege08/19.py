import itertools
from itertools import repeat

for i, s in enumerate(itertools.product('АМРТ', repeat = 4), 1):
    if i == 250:
        print(i,"".join(s))
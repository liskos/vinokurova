import itertools
from itertools import repeat

for i, s in enumerate(itertools.product('КОР', repeat = 5), 1):
    if i == 238:
        print(i,"".join(s))
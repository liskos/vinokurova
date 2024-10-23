import itertools
from itertools import repeat

for i, s in enumerate(itertools.product('КОР', repeat = 5), 1):
    if i == 182:
        print(i,"".join(s))
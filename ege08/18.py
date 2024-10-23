import itertools
from itertools import repeat

for i, s in enumerate(itertools.product('ИОУ', repeat = 5), 1):
    if i == 240:
        print(i,"".join(s))
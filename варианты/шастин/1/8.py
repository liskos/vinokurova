import itertools
from itertools import repeat

for i, a in enumerate(itertools.product('БЕНРСТЬЯ', repeat= 5),1):
    s = "".join(a)
    if i % 2 == 0 and a[0]=='Р' and "Ь" not in a:

        print(i, s)

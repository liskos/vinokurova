import itertools
from itertools import repeat

a = set()
for i in itertools.product('СИРОП', repeat = 5):
    ss = "".join(i).replace("Р", "С").replace("П", "С")
    ss = ss.replace("СО", "XX")
    print(ss)
    if "О" not in ss and i.count("О") == 1:
        a.add(i)

print(len(a))
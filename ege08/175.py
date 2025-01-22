import itertools
from itertools import repeat

for n, i in enumerate(itertools.product("авикнст", repeat = 4), 1):
    s = "".join(i)
    ss = s.replace("в", "с").replace("к", "с").replace("н", "с").replace("т", "с")
    ss = ss.replace("и","а")
    if ss[0] == "с" and ss[-1] == "а":
        print(n, i)


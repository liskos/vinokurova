import itertools
from itertools import repeat
k = 0
for i in itertools.product("авикнст", repeat = 4):
    s = "".join(i)
    ss = s.replace("в", "с").replace("к", "с").replace("н", "с").replace("т", "с")
    ss = ss.replace("и","а")
    if ss[0] == "с" and ss[-1] == "а":
        k +=1
        if s == "ника":
            print(k)


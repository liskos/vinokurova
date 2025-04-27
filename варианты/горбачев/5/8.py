import itertools
k = 0
for i, s in enumerate(itertools.product("wsda", repeat = 5), 1):
    ss = "".join(s)
    if "dd" in ss and ss.count("s") >= 1 and ss[-1] != "w":
        print(i, s)
        break
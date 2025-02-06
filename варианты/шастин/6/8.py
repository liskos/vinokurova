import itertools


for k in range(0, 21):
    t = 0
    for i in itertools.product("01",repeat = 20):
        if i.count("0") == k:
            t += 1
    print(k, t)
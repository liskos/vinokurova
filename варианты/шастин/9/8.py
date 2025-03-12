import itertools

for i, s in enumerate(itertools.product("геинрся", repeat = 6), 1):
    ss = "".join(s)
    if "гиря" in ss:
        print(i, s)
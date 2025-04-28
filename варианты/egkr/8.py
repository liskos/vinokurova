import itertools

for i, s in enumerate(itertools.product("абдеоп", repeat= 6), 1):
    if (i% 2 == 0) and (s[0] == "о") and len(set(s)) == 6:
        print(i, s)
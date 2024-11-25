import itertools

k = 0
for i in itertools.product("0123456789ab", repeat = 6):
    if "0" != i[0] and i.count("b") == 1 and i.count("2")+ i.count("4") + i.count("6") + i.count("8") + i.count("a") + i.count("0") == 3:
        k += 1
print(k)

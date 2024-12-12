import itertools

k = 0
for i in itertools.product("ггс", repeat=6):
    if i[0] == "г":
        k += 1
print(k)
    
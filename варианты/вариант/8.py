import itertools

k = 0
for i in itertools.permutations(range(10), r = 4):
    c = [str(x% 2) for x in i]
    z = "".join(c)
    if i[0] != 0 and "11" not in z and "00" not in z:
        k += 1
print(k)
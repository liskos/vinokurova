
a = set()
for x in range(10000):
    s = 7 ** 270 + 7 **170 + 7 **70 - x
    if str(s).count("0") >= 30:
        a.add(int(s, 7))
print(max(a))
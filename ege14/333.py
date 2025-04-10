n = 81**79 + 75**2022 - 12**35
s = ""
while n > 0:
    s = str(n%5) + s
    n = n//5
print(sum([s.count("4" + str(i)) for i in range(1, 4)]))
n = 19**81 +23 **709 - 4
s = ""
while n > 0:
    s = str(n%9) + s
    n = n//9
print(sum([s.count("8" + str(i)) for i in range(1, 8)]))

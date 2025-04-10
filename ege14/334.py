n = 53**123 + 65**2222 - 172**12
s = ""
while n > 0:
    s = str(n%7) +s
    n =  n//7
print(sum([s.count("6" + str(i)) for i in range(1, 6)]))
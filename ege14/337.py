n = 4*8**3032 + 3*16**1956 +870
s = ""
while n > 0:
    s = str(n%7) + s
    n = n // 7
print(s.count("3") - s.count("1"))
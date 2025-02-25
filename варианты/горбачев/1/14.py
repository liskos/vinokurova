n = 25 * 752  **1274 - 7 * 38**653 - 22 * 51**831 - 7569
s = []
while n > 0:
    s.append(n%9)
    n = n // 9
print(s.count(0))
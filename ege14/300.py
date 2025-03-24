n =  7**103 + 20 **204 - 3*7**57 +97
s = []
while n > 0:
    s.append(n%7)
    n = n // 7
print(s.count(6))

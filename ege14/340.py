n = (7**(9**2-1)-(10-3)**4+int("234", 7))*5/6*8
s = ""
while n > 0:
    s = str(n%7) + s
    n = n//7
print(s.count("4"))
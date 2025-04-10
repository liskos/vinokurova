a = set()
for x in range(1, 10000000):
    if len(hex(x)) <=10 and len(oct(x)) >=13 and x%10 == 5:
        a.add(x)
print(len(a))
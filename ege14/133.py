k = []
for x in range(0, 1000):
    if  str(oct(x))[-3] == "4" and str(oct(x))[-1] == "2" and len(hex(x)[2:]) == 3:
        k.append(x)
print(len(k))
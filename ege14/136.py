k = []
for x in range(0, 1000):
    if  str(oct(x))[-3] == "2" and str(oct(x))[-1] == "6" and len(oct(x)[2:]) == 3 and len(hex(x)[2:]) == 2 and  hex(x)[-1] == "e":
        print(x)
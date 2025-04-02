k = []
for x in range(0, 1000):
    if  str(oct(x))[-2] == "0" and len(oct(x)[2:]) == 3 and len(hex(x)[2:]) == 2 and  hex(x)[-1] == "5":
        print(x)
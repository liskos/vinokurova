k = []
for x in range(0, 1000):
    if  str(oct(x))[-3] == "1" and len(oct(x)[2:]) == 3 and len(hex(x)[2:]) == 3 and hex(x)[-3] == "3" and hex(x)[-1] == "9":
        print(x)
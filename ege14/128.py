for x in range(0, 1000):
    if str(bin(x)[2:])[0:2] == "10" and str(oct(x))[-2] == "4" and str(hex(x))[-1] == "2":
        print(x)
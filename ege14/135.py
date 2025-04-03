k =0
for x in range(0, 1000):
    if len(oct(x)[2:]) == 3 and len(hex(x)[2:]) == 2 and hex(x)[-1] == "a":
        k += 1
        print(x)
print(k)
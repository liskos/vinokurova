k =0
for x in range(0, 1000):
    if len(oct(x)[2:]) == 3 and len(hex(x)[2:]) == 3 and hex(x)[-2] == "a":
        k += 1
        print(x)
print(k)
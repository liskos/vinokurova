def f(n):
    b = bin(n)[2:]
    if b.count("1") > b.count("0"):
        b = b + "0"
    else:
        b = "11" + b
    if b.count("1") > b.count("0"):
        b = b + "0"
    else:
        b = "11" + b
    return int(b, 2)


for i in range(1, 1000):
    if f(i) > 500:
        print(i)
        break
def f(n):
    b = bin(n)[2:]
    b2 = str(b) + str(sum(map(int, str(n))) % 2)
    if b.count("1") > b.count("0"):
        b2 = b2 + "0"
    else:
        b2 = b2 + "1"
    return int(b2, 2)


for i in range(2, 1000):
    if f(i) > 80:
        print(f(i))
        break
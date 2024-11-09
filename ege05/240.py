def f(n):
    n = str(n)
    b = str(bin(int(n[0]))[2:]) + str(bin(int(n[1]))[2:])
    b = b.replace("1", "2")
    b = b.replace("0", "1")
    b = b.replace("2", "0")
    return int(b, 2)


print(f(13))
for i in range(1, 10000):
    if f(i) == 151:
        print(i)
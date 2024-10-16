def f(n):
    b = bin(n)[2:].zfill(8)
    b = b.replace("0", "2")
    b = b.replace("1", "0")
    b = b.replace("2", "1")
    return int(b, 2) - n


print(f(13))
for i in range(0, 256):
    if f(i) == 99:
        print(i)
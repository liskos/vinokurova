def f(n):
    b = bin(n-1)[2:].zfill(8)
    b = b.replace('1', '2')
    b = b.replace('0', '1')
    b = b.replace('2', '0')
    return int(b, 2)

for i in range(1, 256):
    if f(i) == 113:
        print(i)
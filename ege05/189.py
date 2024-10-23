def f(n):
    b = bin(n)[2:].zfill(8)
    after = b[b.rfind('1'):]
    before = b[:b.rfind('1')]
    before = before.replace('1', '2')
    before = before.replace('0', '1')
    before = before.replace('2', '0')
    b = before + after
    return int(b, 2)

for i in range(1, 256):
    if f(i) == 98:
        print(i)
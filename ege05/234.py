def f(n):
    b = bin(n)[2:]
    if b.count("1") > b.count("0"):
        b = b + "0"
    else:
        b = b +"1"
    if len(b) % 2 == 0:
        r = b[:len(b) // 2 - 1] + b[len(b) // 2 + 1:]
    else:
        r = b[:len(b) // 2 - 1] + b[len(b) // 2 + 2:]
    return int(r, 2)

k = 0
for i in range(4, 1000):
    if 50 <= f(i) <= 100 :
        k +=1
        print(f(i))
print(k)
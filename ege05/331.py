def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = b.replace("1", "2").replace("0", "1").replace("2", "0")
    else:
        b = b
    b = 
    return int(b, 2)

print(f(5))
for i in range(1, 1000):
    if f(i) > 60:
        print(i)
        break
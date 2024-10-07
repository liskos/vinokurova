def f(n):
    b = bin(n)[2:]


for i in range(1, 1000):
    if f(i) > 100:
        print(i)
        break

def f(n):
    if n//1000 % 2 == 0:
        return n // 1000 + n // 10 % 10 + abs(n //100 % 10 - n % 10)
    else:
        return bin(n)[2:].count("1")

k = 0
for i in range(1000, 10000):
    if f(i) > 20:
        k += 1
print(k)
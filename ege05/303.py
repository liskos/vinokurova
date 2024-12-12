def f(n):
    if (n // 1000) % 4 == 0:
        n = "9" + str(n % 1000)
    elif (n // 1000) % 2 == 0 and (n // 1000) % 4 != 0:
        n = "3" + str(n%1000)
    return int(n)

k = 0
for i in range(1000, 9999+1):
    if str(f(i))[0] == "9" and f(i) % 8 == 4:
        k += 1
print(k)
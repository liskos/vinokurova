def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '00'
    else:
        b = b + "11"
    return int(b, 2)



for i in range(1, 1000):
    if f(i) > 115:
        print(i)
        break
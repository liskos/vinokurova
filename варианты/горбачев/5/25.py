
def m(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return i + n // i
    return 0

k = 0
for i in range(159870, 900000):
    if str(m(i))[0] == "7" and str(m(i))[-1] == "7":
        k+= 1
        print(i, m(i))
        if k == 7:
            break
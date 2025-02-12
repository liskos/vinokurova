def f(n):
    d = n //1000
    s1 = d * ((n//100)%10)
    s2 = d * ((n % 100 )//10)
    s3 = d * (n%10)
    m = sorted([s1, s2, s3])
    return str(s2) + str(s3)

print(f(2345))
for i in range(1000, 9999+1):
    if f(i) == "5472":
        print(i)




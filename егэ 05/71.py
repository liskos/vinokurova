def f(a,b):
    a = str(a)
    b = str(b)
    s1 = int(a[0]) + int(b[0])
    s2 = int(a[1]) + int(b[1])
    s3 = int(a[2]) + int(b[2])
    m =  sorted([s1, s2, s3], reverse=True)
    return str(m[0]) + str(m[1]) + str(m[2])

print(f(835, 196))    
for i in range(100, 1000):
    if f(i,694) == '11108':
        print(i)
        break
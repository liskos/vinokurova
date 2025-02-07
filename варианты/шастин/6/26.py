def f(filename):
    file = open(filename)
    n = int(file.readline())
    t = [0] * 24 * 60
    r = [[] for _ in range(24 * 60)]
    for _ in range(n):
        id, t1, t2 =  map(int, file.readline().split())
        for x in range(t1, t2):
            t[x] += 1
            r[x].append(id)
    m = max(t)
    b = []
    for x in range(1, 24*60-1):
        if t[x] == m and t[x-1] != m:
            b.append([x])
        if t[x]==m and t[x+1] != m:
            b[-1].append(x)
    print(b)
    b = sorted(b, key=lambda x:x[1]-x[0], reverse=True)
    print(b[0])
    z = set()
    for x in range(b[0][0], b[0][1]+1):
        z |= set(r[x])
    print(z)
    return len(b), sum(z)



print(f("26.txt"))
print("______")
print(f("26test.txt"))

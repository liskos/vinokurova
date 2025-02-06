def f(filename):
    file = open(filename)
    n = int(file.readline())
    t = [0] * 24 * 60
    for _ in range(n):
        id, t1, t2 =  map(int, file.readline().split())
        for x in range(t1, t2):
            t[x] += 1
    m = max(t)
    for x in range(24*60):
        if t[x] == m:
            print(x)
    return 0, 0



print(f("26.txt"))
print("______")
print(f("26test.txt"))

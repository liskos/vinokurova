def f(n):
    h = hex(n)[2:]
    if n % 2 == 0:
        h = h + max(h)
    else:
        h = h +"0"
    h = h + str(sum(map(int, str(h))) % 16)
    h = h + str(sum(map(int, str(h))) % 16)
    return h

for i in range(1, 10000):
    if (f(i).count(min(f(i))) // f(i).count((max(f(i))))) == 5:
        print(i)
        break
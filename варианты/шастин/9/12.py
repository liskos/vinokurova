def f(s):
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    return s

for n in range(7, 100):
    s =  ">" + 19*"0" + n * "1" + 19*"2"
    r = f(s)[:-1]
    summa = sum(map(int, r))
    if str(summa)[-1] == str(summa)[-2]:
        print(n)
        break
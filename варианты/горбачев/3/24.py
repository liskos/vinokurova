def f(s):
    m = 0
    t = ""
    kA = 0
    for i in s:
        t += i
        if i == "A":
            kA += 1
        while (kA > 22):
            if t  and t[0] == "A":
                kA -= 1

            t = t[1:]
        if s.count("A") == 22:
            m = max(m, len(t))
    return m

s = open("24.txt").read()
m = 0

for x in s.split("F"):
    m = max(m, f(x))
print(m)
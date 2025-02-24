s = open("24.txt").read()
t = ""
m = 0
for i in s:
    t += i
    while t.count("WWF") > 120 or "WSFWW" in t:
        t = t[1:]
    m = max(m, len(t))
print(m)
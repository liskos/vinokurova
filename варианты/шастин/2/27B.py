import sys, funk27
sys.stdin = open("27B.txt")
kl_a = []
kl_b = []
kl_c = []
kl_d = []
kl_e = []
for _ in range(10000):
    x, y = map(float, input().split())
    if x > 12:
        kl_a.append([x,y])
    elif y > 14:
        kl_b.append([x,y])
    elif y > 10:
        kl_c.append([x, y])
    elif y > 6:
        kl_d.append([x,y])
    else:
        kl_e.append([x, y])
d, sx, sy = funk27.f(kl_b, kl_c)
print(d, int(sx* 1000), int(sy* 1000))
d, sx, sy = funk27.f(kl_c, kl_d)
print(d, int(sx* 1000), int(sy* 1000))
d, sx, sy = funk27.f(kl_d, kl_e)
print(d, int(sx* 1000), int(sy* 1000))
import sys, funk27
sys.stdin = open("27A.txt")
kl_a = []
kl_b = []
for _ in range(96):
    x, y = map(float, input().split())
    if x < 1:
        kl_a.append([x,y])
    else:
        kl_b.append([x,y])
d, sx, sy = funk27.f(kl_a, kl_b)
print(int(sx* 1000), int(sy* 1000))
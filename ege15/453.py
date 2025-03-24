k = 10
p = range(10*k, 20*k+1)
q = range(4*k, 40*k+1)
a1_best = 0
a2_best = 100*k
for a1 in range(8*k, 12*k):
    for a2 in range(18*k, 22*k):
        a = range(a1, a2+1)
        if (a2-a1 < a2_best-a1_best) and all([((x not in a) and not(not(x in p) or (x not in q))) == False for x in range(0, 100*k)]):
            a1_best = a1
            a2_best = a2
print(a1_best/k, a2_best/k, (a2_best-a1_best)/k)

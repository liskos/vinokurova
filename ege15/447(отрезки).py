p = range(10, 25+1)
q = range(28, 40+1)
a1_best = 0
a2_best = 100
for a1 in range(0, 100):
    for a2 in range(a1, 100):
        a = range(a1, a2+1)
        if (a2-a1 < a2_best-a1_best) and all([(not ((x in p) and (x not in a)) or ( x not in q)) for x in range(0, 100)]):
            a1_best = a1
            a2_best = a2
print(a1_best, a2_best, a2_best-a1_best)

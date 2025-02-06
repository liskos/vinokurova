k = 10
c = range(48*k, 94*k+1)
j = range(83*k, 100*k+1)
besta1 = 0
besta2 = 0
for a1 in range(45*k, 50*k):
    for a2 in range(95*k, 105*k):
        a = range(a1, a2+1)
        if all((x in c) or (x in j)or x not in a for x in range(1, 150*k)):
            if a2-a1>besta2-besta1:
                besta2 = a2
                besta1 = a1
print(besta1/k, besta2/k, (besta2-besta1)/k)
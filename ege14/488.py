r = []
for x in range(2, 2025+1):
    s = 5**2025+5**200-x
    k = 0
    while s > 0:
        if s%5 == 4:
            k +=1
        s = s//5
    r.append([k, x])
print(max(r, key= lambda x:(x[0],x[1])))


def f(x,y):
    return (x-3, y), ((x+1)//2, y), (x, y-3), (x,(y+1)//2)

a = [[" "] * 1200 for i in range(1200)]
for i in range(1200):
    for j in range(1200):
        if i + j <=72:
            a[i][j] = "0"

for i in range(1200):
    for j in range(1200):
        if a[i][j] == " " and  any(a[x][y]=="0" for x,y in f(i, j)):
            a[i][j] = "1"
for i in range(1200):
    for j in range(1200):
        if a[i][j] == " " and all(a[x][y]=="1" for x,y in f(i, j)):
            a[i][j] = "2"
for i in range(1200):
    for j in range(1200):
        if a[i][j] == " " and any(a[x][y]=="2" for x,y in f(i, j)):
            a[i][j] = "3"
for i in range(1200):
    for j in range(1200):
        if a[i][j] == " " and all(a[x][y] in "13" for x,y in f(i, j)):
            a[i][j] = "4"

import sys
sys.stdout = open("19-21.xls", mode = "w" )
for i in range(1, 1200):
    print(*a[i][1:], sep ="\t")
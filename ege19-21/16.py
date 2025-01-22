def f(x,y):
    return (x+2, y), (x*2, y), (x, y+2), (x,y*2)

a = [[" "] * 200 for i in range(200)]
for i in range(200):
    for j in range(200):
        if i + j >= 61:
            a[i][j] = "0"

for i in range(61):
    for j in range(61):
        if a[i][j] == " " and  any(a[x][y]=="0" for x,y in f(i, j)):
            a[i][j] = "1"
for i in range(61):
    for j in range(61):
        if a[i][j] == " " and all(a[x][y]=="1" for x,y in f(i, j)):
            a[i][j] = "2"
for i in range(61):
    for j in range(61):
        if a[i][j] == " " and any(a[x][y]=="2" for x,y in f(i, j)):
            a[i][j] = "3"
for i in range(61):
    for j in range(61):
        if a[i][j] == " " and all(a[x][y] in "13" for x,y in f(i, j)):
            a[i][j] = "4"

import sys
sys.stdout = open("16.xls", mode ="w")
for i in range(1, 200):
    print(*a[i][1:], sep ="\t")
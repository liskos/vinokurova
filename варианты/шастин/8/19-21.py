def f(x,y):
    return (x-3, y-3), (x//2, y), (x, y//2)

a = [[" "] * 1000 for i in range(1000)]
for i in range(1000):
    for j in range(1000):
        if i + j >= 87:
            a[i][j] = "0"

for i in range(87):
    for j in range(87):
        if a[i][j] == " " and  any(a[x][y]=="0" for x,y in f(i, j)):
            a[i][j] = "1"
for i in range(87):
    for j in range(87):
        if a[i][j] == " " and all(a[x][y]=="1" for x,y in f(i, j)):
            a[i][j] = "2"
for i in range(87):
    for j in range(87):
        if a[i][j] == " " and any(a[x][y]=="2" for x,y in f(i, j)):
            a[i][j] = "3"
for i in range(83):
    for j in range(87):
        if a[i][j] == " " and all(a[x][y] in "13" for x,y in f(i, j)):
            a[i][j] = "4"

import sys
sys.stdout = open("3.xls", mode ="w")
for i in range(1, 200):
    print(*a[i][1:], sep ="\t")
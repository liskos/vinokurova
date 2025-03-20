def f(x,y):
    return (x-2, y), ((x//3), y), (x, y-2), (x,(y//3))

a = [[" "] * 1500 for i in range(1500)]
for i in range(1500):
    for j in range(1500):
        if i < 15 or j < 15:
            a[i][j] = "0"

for i in range(1500):
    for j in range(1500):
        if a[i][j] == " " and  any(a[x][y]=="0" for x,y in f(i, j)):
            a[i][j] = "1"
for i in range(1500):
    for j in range(1500):
        if a[i][j] == " " and all(a[x][y]=="1" for x,y in f(i, j)):
            a[i][j] = "2"
for i in range(1500):
    for j in range(1500):
        if a[i][j] == " " and any(a[x][y]=="2" for x,y in f(i, j)):
            a[i][j] = "3"
for i in range(1500):
    for j in range(1500):
        if a[i][j] == " " and all(a[x][y] in "13" for x,y in f(i, j)):
            a[i][j] = "4"

for s in range(1, 1500):
    if a[s][s] == "2":
        print("2:", s, end=" ")
for i in range(1, 1500):
    for s in range(1, 1500):
        if a[i][s] == "3":
            print(s)
#
# import sys
# sys.stdout = open("19-21.xls", mode ="w")
# for i in range(1, 1500):
#     print(*a[i][1:], sep ="\t")
def f(x,y):
    return (x-3, y-3), (x//2, y), (x, y//2)

a = [[" "] * 1000 for i in range(1000)]
for i in range(1000):
    for j in range(1000):
        if i + j <= 100:
            a[i][j] = "0"

for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and  any(a[x][y]=="0" for x,y in f(i, j)):
            a[i][j] = "1"
for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and all(a[x][y]=="1" for x,y in f(i, j)):
            a[i][j] = "2"
for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and any(a[x][y]=="2" for x,y in f(i, j)):
            a[i][j] = "3"
for i in range(1000):
    for j in range(1000):
        if a[i][j] == " " and all(a[x][y] in "13" for x,y in f(i, j)):
            a[i][j] = "4"

for s in range(53, 1000):
    if any(a[i][j] == "1" for i, j in f(48, s)):
        print(s)
        break

for s in range(53, 1000):
    if a[48][s] == "3":
        print(s, end=" ")

print()
for s in range(53, 1000):
    if a[48][s] == "4":
        print(s, end=" ")
# import sys
# sys.stdout = open("19-21.xls", mode ="w")
# for i in range(1, 1000):
#     print(*a[i][1:], sep ="\t")
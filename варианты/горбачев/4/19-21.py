def f(x,y):
    return (x-1, y), (x//3, y), (x, y//3),  (x, y-1)

k = 1000
a = [[" "] * k for i in range(k)]
for i in range(k):
    for j in range(k):
        if i + j < 64:
            a[i][j] = "0"

for i in range(k):
    for j in range(k):
        if a[i][j] == " " and  any(a[x][y]=="0" for x,y in f(i, j)):
            a[i][j] = "1"
for i in range(k):
    for j in range(k):
        if a[i][j] == " " and all(a[x][y]=="1" for x,y in f(i, j)):
            a[i][j] = "2"
for i in range(k):
    for j in range(k):
        if a[i][j] == " " and any(a[x][y]=="2" for x,y in f(i, j)):
            a[i][j] = "3"
for i in range(k):
    for j in range(k):
        if a[i][j] == " " and all(a[x][y] in "13" for x,y in f(i, j)):
            a[i][j] = "4"


print([i for i in range(7, k) if a[57][i] == "2"])
print([i for i in range(7, k) if a[57][i] == "3"])
print([i for i in range(7, k) if a[57][i] == "4"])

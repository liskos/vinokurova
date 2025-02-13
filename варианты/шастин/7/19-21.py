def f(x):
    return x+3, x*3, x+(x**2)


a = [" "] * 665*665
for i in range(665*665):
    if i > 665:
        a[i] = "0"

for i in range(665*665):
    if a[i] == " " and  any(a[x]=="0" for x in f(i)):
        a[i] = "1"
for i in range(665*665):
    if a[i] == " " and all(a[x]=="1" for x in f(i)):
        a[i] = "2"
for i in range(665*665):
    if a[i] == " " and  any(a[x]=="2" for x in f(i)):
        a[i] = "3"
for i in range(665*665):
    if a[i] == " " and all(a[x] in "13" for x in f(i)):
        a[i] = "4"


print([i for i in range(1, 3000) if a[i] == "1"])
print([i for i in range(1, 3000) if a[i] == "3"])
print([i for i in range(1, 3000) if a[i] == "4"])
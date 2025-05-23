import re
s = open("24.txt").read()
pattern = r"([1-9A-D][0-9A-D]*[02468AC])"
r = [x.group() for x in re.finditer(pattern, s)]
m = 0
for x in r :
    m = max(m, int(x, 14))
for x in r :
    if int(x, 14) == m:
        print(len(x), x)
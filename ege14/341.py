n = 4*625**1920+4*125**1930 - 4*25**1940 - 3*5**1950 - 1960
s = ""
while n >0:
    s = str(n %5) +s
    n = n//5
print(s.count("0"))
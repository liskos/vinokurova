n = 13*625**1320 + 12*125**1230 - 14*25**1140 - 13*5**1050 - 2500
s = ""
while n >0:
    s = str(n%25)+s
    n = n //25
print(s.count("0"))
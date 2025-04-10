n = 7*5**1984 - 6*25**777 + 5*125**333 -4
s = ''
while n > 0:
    s = str(n%5) +s
    n = n //5
print(len(s)-1)
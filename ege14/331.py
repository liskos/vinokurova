n = 8**888+ 15*15**1515-2**444
s = ""
while n > 0:
    s = str(n%8)+s
    n = n//8
print(sum([s.count("7" + str(i)) for i in range(1, 7)]))
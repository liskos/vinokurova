n = 7*512**3200+6*256**3100-5*64**3000-4*8**2900-1542
s = ""
while n > 0:
    s = str(n%64) +s
    n = n//64
print(s.count("0"))
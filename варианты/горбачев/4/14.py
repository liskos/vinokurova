n = 9 *123**2053 + 5*23**3146+91*47**5533+4099
t = '0123456789abcdefghijklmn'
s = ""
while n > 0:
    s = t[n%23] + s
    n = n // 23
print(s.count("g")+s.count("h")+s.count("i")+s.count("j")+s.count("k")+s.count("l")+s.count("m")+s.count("n"))

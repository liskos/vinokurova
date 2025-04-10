for x in range(1,1000):
    for y in range(1, 1000):
        s = (3+2*4**x)* 4 **x+3+4**y
        ss = []
        while s > 0:
            ss.append(s % 4)
            s = s // 4
print(max(str(ss)))
    
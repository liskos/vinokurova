for x in range(3, 100):
    s = (88+2*8**x)*8**x+88+8**8
    r = oct(s)[2:]
print(r)
print(sum(map(int, str(r))))
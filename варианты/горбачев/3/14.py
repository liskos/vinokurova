for x in range(1, 3052):
    s = 4**151 + 7**283 + 6 **82 - 5*x
    k = 0 # кол-во 1 в восьмиричной системе
    while s > 0:
        if s % 8 == 1:
            k += 1
        s = s //8
    if k == 26:
        print(x)
        break
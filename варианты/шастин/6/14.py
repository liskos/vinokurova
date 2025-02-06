for x in range(0, 25):
    s1 = int("a407f2", 25) + x*25**3
    s2 =  int("n0g50h", 25) + x* 25**4 +x*25
    s3 = int("740m26", 25) + x*25**3
    if (s1 +s2 +s3) % 24 == 0:
        print(x, (s1+s2+s3)//24)
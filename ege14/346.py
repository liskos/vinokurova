for x in range(0, 15):
    s = int("12305", 15)+ x*15 + int("10233", 15) +x*15**3
    if s % 14 ==0:
        print(s//14)
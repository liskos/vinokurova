for x in range(0,15):
    for y in range(0, 17):
        s =int("12305", 15)+ x*15 + int("6709", 17) + y*17
if s%131 == 0:
    print(s//131)
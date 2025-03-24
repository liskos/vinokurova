for a in range(1, 100):
    if all((x % a == 0) or ((x % 6 != 0) or (x % 4 != 0))  for x in range(1, 100)):
        print(a)
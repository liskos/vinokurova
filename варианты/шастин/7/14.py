for a in range(1, 2000000):
    for x in "0123456789abcde":
        m = int(f"432{x}3", 15)
        n = int(f"86{x}86", 15)
        if (a + m) % n == 0:
          print(a)
          break


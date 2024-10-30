for x in "0123456789abcdefghijklmn":
    s = int(f"12{x}734", 24) + int(f"8{x}95{x}3", 24) + int(f"24{x}796", 24)
    if s % 23 == 0:
        print(s // 23)
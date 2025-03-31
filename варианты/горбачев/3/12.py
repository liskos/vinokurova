def f(s:str):
    while ("-+" in s) or ("2++" in s) or ("++++" in s):
        if "-+" in s:
            s = s.replace("-+", "2+", 1)
        if "2++" in s:
            s = s.replace("2++", "--", 1)
        if "++++" in s:
            s = s.replace("++++", "22", 1)
    return s


for n in range(1, 1000):
    s = "-" + "+" * n
    rez = f(s)
    if rez.count("+") + rez.count("-") == 251:
        print(n)

s = open("24.txt").read()

import re
number = r"(([1-9][0-9]*)|[0])"
pattern = rf"{number}([*+]{number})*"
r = [x.group() for x in re.finditer(pattern, s)]
m = max(r, key=len)
print(r[:10])
print(len(m))
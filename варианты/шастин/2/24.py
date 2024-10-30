import sys
sys.stdin = open("24.txt")
s = input().split("X")
a = max([x.count("Y") for x in s])
b = [x for x in s if x.count("Y") == 75]
print(s)
print(a)
print(len(b[1])) # + 2 x
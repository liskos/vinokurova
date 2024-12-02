def solushen(a, b, c, d):
    s = sorted([a, b, c, d])
    if s[0] / s[2] + s[1] / s[3] < s[1] / s[3] + s[0] / s[2]:
        return  s[1], s[3], s[0], s[2]
    else:
        return s[0],s[2], s[1], s[3],

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    print(solushen(a, b, c, d))
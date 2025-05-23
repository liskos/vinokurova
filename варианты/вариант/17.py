a = [int(i) for i in open("17.txt")]
m = [i for i in a if str(i)[-2:] == "15" and len(str(abs(i))) ==  3]
r = []
for t in zip(a, a[1:], a[2:]):
    if ((t[0] > 0 and t[1]> 0 and t[2] > 0) or  (t[0]< 0 and t[1]< 0 and t[2] < 0)) and min(t) * max(t) > min(m)**2:
        r.append(max(t) *min(t))
print(len(r), min(r))


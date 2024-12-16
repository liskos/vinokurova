import itertools

a = set()
for i in itertools.permutations("нода", r = 4):
    s = "".join(i)
    if s.count("оа") == 0 and s.count("ао") == 0 and s.count("нд") == 0 and s.count("дн") == 0:
        a.add(i)
        print(i)
print(len(a))
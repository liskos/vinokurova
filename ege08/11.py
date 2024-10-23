import itertools
from itertools import repeat

for i, s in enumerate(itertools.product('АОУ', repeat = 5), 1):
    if s[0] == "У" and s[1] == "А" and s[2] == "У" and s[3] == "А" and s[4] == "У":
        print(i, s)
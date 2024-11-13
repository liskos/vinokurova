import itertools
from itertools import repeat

for i in itertools.product("АБВГЭЮЯ", repeat=5):
    if i.count("Э") <= 2 and "Э"

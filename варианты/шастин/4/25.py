import fnmatch

for i in range(1996, 10**10, 1996):
    if fnmatch.fnmatch(str(i), "1592*6?8"):
        print(i,i//1996)
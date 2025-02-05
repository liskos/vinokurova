from audioop import reverse
f = open("26.txt")
n, m = map(int, f.readline(). split()) # n  - число снарядов, m - число атлетов
vesa_sn = [int(f.readline()) for _ in range(n)]  # сичтываем веса снарядов имеющихся
vesa_at = [int(f.readline()) for _ in range(m)] # считываем веса которые могут быть полнятые отлетами
a = dict() # словарь поднтых весов (количество), ключ это вес
for i in range(n):
    a[vesa_sn[i]] = 0
vesa_sn.sort() # сортируем по возрастанию снаряды
vesa_at.sort() # сортируем по возрастанию максимальные веса атлетов
j = 0
for i in range(m): # перебираем веса атлетов
    while vesa_sn[j] <= vesa_at[i]: # пока снаряд меньше максимального веса алетов
        j +=1
    j -= 1 # берем предыдущий поднятый снаряд
    a[vesa_sn[j]] += 1 # в словарь добавляем 1 к количеству поднятых
print(a)
s = 0
k = 0
for x in a:
    s += x *a[x] # добавляем поднятые веса
    k += a[x]    #  добавляемся кол-во раз поднятых
s = s/ k         # среднй поднятый вес
z = max(a, key= lambda x:a[x])
print(int(s), z)


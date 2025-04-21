file = open("26.txt")
n, m, k = map(int, file.readline().split())
print(f'число занятых мест {n}')
print(f'кол-во рядов {m}')
print(f"кол-во мест в ряду {k}")
a = [100000] * (k+1)
for _ in range(n):
    nomer_row, nomer_column = map(int, file.readline().split())
    a[nomer_column] = min(a[nomer_column], nomer_row )

b = []
for i in range(1, len(a)-3):
    b.append([min(a[i], a[i+1], a[i+2], a[i+3]), i+3])
print(max(b, key=lambda x:(x[0], x[1])))
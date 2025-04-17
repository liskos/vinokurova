file = open("26.txt")
n =  int(file.readline())
print(f'число товаров {n}')
a = [int(file.readline()) for _ in range(n)]
a.sort(reverse=True)
print(f'товары {a[:20]}')
k = n // 5
print(f"количество товаров со скидкой {k}")
s1 = sum(a[:k]) * 0.5 + sum(a[k:])
print(f"хотел заплатить покупатель {s1}")
s2 = sum(a) - sum(a[4::5])*0.5
print(f"заплатил покупатель после перестановки {s2}")
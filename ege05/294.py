from audioop import reverse


def f(n):
    if n % 2 == 0:
        s = [n]
        return int(n.sort(reverse=True)) // 2
    else:
        s = [n]
        return int(n.sort(reverse=False)) * 2
print(f(1488))
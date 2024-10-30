def f(kl_a, kl_b):
    d = 10
    xa = 0
    xb = 0
    ya = 0
    yb = 0
    for x1, y1 in kl_a:
        for x2, y2 in kl_b:
            s = ((x1 - x2)**2 + (y1-y2)**2) ** 0.5
            if s < d:
                d = s
                xa = x1
                ya = y1
                xb = x2
                yb = y2
    return d, xa + xb, ya +yb

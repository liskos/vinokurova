import math, turtle

def clasterization(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1, p2) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return min(r)[1]

def get_centroid_transf(data, centers):
    r = []
    for p1 in data:
        r += [(sum(math.dist(p1, p2) for p2 in centers), p1)]
    return min(r)[1]

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "green", "pink", "black", "orange"]
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x*30, y *30)
            turtle.dot(5, colors[i % len(colors)])
    turtle.done()


data = [list(map(float,line.split())) for line in open("27A.txt")]
clasters = clasterization(data.copy(), 0.4)
centers = [get_centroid(c) for c in clasters]
x, y = get_centroid_transf(data, centers)
print(x*10000, y *10000)
#0,4


data = [list(map(float,line.split())) for line in open("27B.txt")]
clasters = clasterization(data.copy(), 0.1)
centers = [get_centroid(c) for c in clasters]
x, y = get_centroid_transf(data, centers)
print(x*10000, y *10000)
#0,1
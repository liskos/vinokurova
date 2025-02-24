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
    pass

def get_centroid_transf(cenrts, data):
    pass

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
clasters = clasterization(data, 0.4)
visual(clasters)
#0, 4
#0,1
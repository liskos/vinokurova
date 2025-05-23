def f1(): return  24
def f2(): return 20
def f3(): return f10() + 19
def f4(): return 22
def f5(): return f2() +  25
def f6(): return max(f4(), f5(), f7(), f8()) + 23
def f7(): return f5() + 18
def f8(): return max(f1(), f5()) + 22
def f9(): return max(f3(), f4()) + 21
def f10(): return f7() + 19
def f11(): return f15() + 22
def f12(): return f9() +  24
def f13(): return max(f10(), f12()) + 25
def f14(): return max(f11(), f15()) + 20
def f15(): return 24
def f16(): return f13() + 25
def f17(): return max(f14(), f16()) + 22

print(max(f1(), f2(), f3(), f4(), f5(), f6(), f7(), f8(),f9(), f10(), f11(), f12(), f13(), f14(), f15(), f16(), f17()))
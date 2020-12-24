def f():
    print("v1")

f1 = f;


def f():
    print("v2")

f2 = f


f1()
f2()
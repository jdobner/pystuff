from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from multiprocessing.pool import Pool
from ctypes import Structure, c_double

class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]

def modify(n, x, s, A):
    n.value **= 2
    x.value **= 2
    s.value = s.value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2

if __name__ == '__main__':
    lock = Lock()

    n = Value('i', 7)
    x = Value(c_double, 1.0/3.0, lock=False)
    s = Array('c', b'hello world', lock=lock)
    A = Array(Point, [(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock=lock)

    with Pool(1) as p:
        p.apply(func=modify, args=(n, x, s, A))


    print(n.value)
    print(x.value)
    print(s.value)
    print([(a.x, a.y) for a in A])
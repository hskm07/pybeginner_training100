from time import time

def bench(func):
    time1 = time()
    func()
    time2 = time()
    label = func.__doc__ or func.__name__
    print("%s: %.3f sec" % (label, time2-time1))

@bench
def normal_append():
    buf = []
    for i in range(1,1000000):
        buf.append(i)
    del buf

@bench
def list_comprehension():
    buf = [i for i in range(1,1000000)]
    del buf

@bench
def reuse_method():
    buf = []
    append = buf.append
    for i in range(1,1000000):
        append(i)
    
    del append
    del buf
    

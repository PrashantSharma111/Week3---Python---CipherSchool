def fun(n):
    return [ i**2 for i in range(1, n) ]

for i in fun(8):
    print(i, end = " ")
print()
# for i in fun(1000000000000000):
    # print(i, end = " ")

def fun(n):
    for i in range(1, n):
        yield i**2
# for i in fun(1000000000000000):
    # print(i, end = " ")

def fun():
    print("Started")
    yield 1
    print("Yielded 1")
    yield 2
    print("Yielded 2")

it = iter(fun())
next(it)
next(it)

from time import sleep
def fun():
    print("Started")
    yield
    sleep(5)
    print("Ended")

it = iter(fun())
next(it)

a = ( i**2 for i in range(10) )
print(type(a), a)              
print(type(iter(a)), a)        
for i in a:
    print(i, end = " ")
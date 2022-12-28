class A:
    def _init_(self):
        print("A's init was executed")

class B(A):
    def _init_(self):
        print("B's init was executed")
        super()._init_()

ob = B()

class A:
    pass
class B(A):
    x = 5
class C(B):
    pass
class D(A):
    x = 10
class E(C, D):
    pass

e = E()
print(E.mro())
print(e.x)

a = range(8)
it = a._iter_()               
print(it._next_())         
print(it._next_())    
print(it._next_())    
print(it._next_())    
print(it._next_())    
print(it._next_())    
print(it._next_())    
print(it._next_())

class myrange:
    def _init_(self, n):
        self.n = n
    
    def _iter_(self):
        return myiter(self)

class myiter:
    def _init_(self, myr):
        self.myr = myr
        self.i = 0

    def _next_(self):
        ret = self.i
        self.i += 1
        
        if (ret >= self.myr.n):
            raise StopIteration

        return ret

a = myrange(8)
it = iter(a)
print(next(it))     # 0
print(next(it))     # 1
print(next(it))     # 2
print(next(it))     # 3
print(next(it))     # 4
print(next(it))     # 5
print(next(it))     # 6
print(next(it))     # 7

for i in myrange(8):
    print(i)
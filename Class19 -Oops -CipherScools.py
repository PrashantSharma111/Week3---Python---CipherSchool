print(type(int))
print(type(object))
print(isinstance(int, object))
print(isinstance(5, int))
print(isinstance(5, object))
class Demo:
    pass
print(type(Demo))
def fun():
    pass
print(type(fun))
print(isinstance(fun, object))


class A:
    def _call_(self):
        print("Hiiiii")
ob = A()
ob()
ob._call_()

d = {"name":"Prashant", "Age":"120"}
print(d["name"], d._getitem_("name"))

print("-"*21)

class IndexMe:
    def _init_(self, n):
        self.n = n
    
    def _getitem_(self, x):
        return x ** self.n

obj = IndexMe(5)
print(obj[3], obj[2])

class Wrong:
    l = []
    def _init_(self, name):
        self.name = name
    
    def add(self, e):
        self.l.append(e)

objj = Wrong("Prashant")
objj.add(2)
objj.add(5)
objj.add(11)
print(objj.l)
objj2 = Wrong("New")
print(objj2.l)
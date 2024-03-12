class Base :
    def __init__(self):
        self._a = 2

class Derived(Base) :
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class  : ",self._a)
        self._a=3

        print("Calling modified member of base class  : ",self._a)

obj1 = Derived()
obj = Base()


print("Accessing protected member of obj : ",obj._a)
print("Accessing protected member of obj1 : ",obj1._a)

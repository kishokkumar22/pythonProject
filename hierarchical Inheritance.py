class parent() :
    def fun(self):
        print("the function in the parent class.")

class child1(parent):
    def fun1(self):
        print("the function in the child1 class.")

class child2(parent) :
    def fun2(self):
        print("the function in the child2 class.")

class child3(parent) :
    def fun3(self):
        print("the function in the child3 class.")

object1 = child1()
object2 = child2()
object3 = child3()

print("object 1 functions")
object1.fun1()
object1.fun()
print("object 2 functions")
object2.fun()
object2.fun2()
print("object 3 functions")
object3.fun()
object3.fun3()
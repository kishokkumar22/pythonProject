class parent() :
    def fun(self):
        print("the function in the parent class.")

class child(parent):
    def fun1(self):
        print("the function in the child class.")

class grandchild(child) :
    def fun2(self):
        print("the function in the grandchild class.")


object1 = child()
object2 = grandchild()
object1.fun()
object1.fun1()
object2.fun2()
object2.fun()
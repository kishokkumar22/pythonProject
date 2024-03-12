class parent() :
    def fun(self):
        print("the function in the parent class.")

class parent1():
    def fun1(self):
        print("the function in the parent1 class.")

class child(parent,parent1) :
    def fun2(self):
        print("the function in the child class.")


object1 = child()
object1.fun()
object1.fun1()
object1.fun2()
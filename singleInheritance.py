class parent() :
    def fun(self,name,age):
        self.name = name
        self.age = age
        print("the function in the parent class.")
@property
class child(parent) :
    def fun1(self):
        print(f"My name is {self.name}")
        print("The function in the child class.")

object1 = child()
object1.fun("Ram",10)
object1.fun1()
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def msg(self):
        return print(f"Name : {self.name}  Age : {str(self.age)}")
    @staticmethod
    def welcome():
        return print("Welcome to the Python Programming world")


new = Student("Raja", 21)
new.msg()
new.welcome()

new2 = Student("Harini", 22)
new2.msg()
new2.welcome()
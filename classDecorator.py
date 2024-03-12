class Student:
    count= 0
    def __init__(self,name,age):
        self.name= name
        self.age =age
        Student.count += 1

    def printall(self):
        return print(f"Name : {self.name}  Age : {self.age}")


class Student:
    count= 0
    def __init__(self,name,age):
        self.name= name
        self.age =age
        Student.count += 1
    def printall(self):
        return print(f"Name : {self.name}  Age : {str(self.age)}")

    @classmethod
    def total(cls):
        return print(f"Total Admission : {cls.count}")


o = Student("Raja",12)
o.printall()
o.total()
o1 = Student("Harini",22)
o1.printall()
o1.total()
o.total()
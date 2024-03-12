class Student :
    name1 = "Raja"
    age = 25
    def printall(self, gender: object) -> object:
        print("Name : ", Student.name1)
        print("Age : ", Student.age)
        print("Gender : ", gender)

o = Student()
o.printall("Male")
Student.printall(o,"Male")

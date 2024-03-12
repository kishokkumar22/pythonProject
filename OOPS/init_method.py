class user:
    def __init__(self,name):
        print("Create a construcror")
        self.name = name

    def printall(self):
        print("Name : ", self.name)

o = user("Raja")
o.printall()
o2 = user("Harini")
o2.printall()
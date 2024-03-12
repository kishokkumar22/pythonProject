class user :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " year old."

o = user("Harini" , 21)
print(o.name)
print(o.age)
print(o.msg)
o.age = 30
print(o.msg)


'''
To change a function into a property method or function is known as property decorator
'''
class yamaha() :
    def type(self):
        print("R15 version 3")
    def color(self):
        print("Blue")

class duke() :
    def type(self):
        print("Duke 250")
    def color(self):
        print("White with Orange")

def func(obj) :
    obj.type()
    obj.color()

obj_yamaha = yamaha()
obj_duke = duke()
func(obj_yamaha)
print("------------------------------")
func(obj_duke)

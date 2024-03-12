class student :

    def __init__(self,total) :
        self._total = total

    @property
    def average(self) :
       return self._total /5.0
    def getter(self):
        return self._total
    def setter(self,t):

        if t>0 or t<500 :
            print("Invalid total and can't change")
        else :  self._total = t

    total = property(getter, setter)

o = student(450)
print(o.total)
print(o.average)
o.total = 250
print(o.total)
print(o.average)
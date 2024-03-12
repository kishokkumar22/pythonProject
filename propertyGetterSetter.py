class student :

    def __init__(self,total) :
        self._total = total

    @property
    def average(self) :
       return self._total /5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self,t):

        if t>0 or t<500 :
            print("Invalid total and can't change")
        else :  self._total = t


class student :

    def __init__(self,total) :
        self._total = total

    @property
    def average(self) :
       return self._total /5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self,t):

        if t>0 or t<500 :
            print("Invalid total and can't change")
        else :  self._total = t

o = student(450)
print(o.total)
print(o.average)
o.total = 250
print(o.total)
print(o.average)
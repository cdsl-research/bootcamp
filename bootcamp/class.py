import math
class A:
    def __init__(self,num):
        self.num = num

    def exp(self):
        print(math.exp(self.num))

    def sqrt(self):
        print(math.sqrt(self.num))

    def log(self):
        print(math.log(self.num))

class B:
    pass

a = A(5)
a.exp()
a.sqrt()
a.log()

B = B()


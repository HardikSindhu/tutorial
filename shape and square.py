class shape:
    def __init__(self):
     print("i am in shape class")
    def area(self):
       return 0
class square(shape):
    def __init__(self,length):
         self.l=length
    def area(self):
         print(self.l*self.l)
    s1=shape()
    s1.area()
    s2=square(10)
    s2.area()

class Rectangle:
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def area_peri(self):
        self.rarea=self.l*self.b
        self.rperi=2*(self.l+self.b)
        return self.rarea
    def disp(self):
        print("area of rectangle is %0.2f"%self.rarea)
        print("perimeter of rectangle is %0.2f"%self.rperi)
class Box(Rectangle):
    def __init(self,l,w,h):
        self.h=h
        super().__init__(l,w)
    def barea_bperi_bvol(self):
        self.barea=2*(self.l*self.w+self.l*self.h+self.h+self.w)
        self.bvol=self.h*super().area_peri()
        self.bperi=4*(self.l+self.b+self.h)
    def disp(self):
        super().disp()
        print("area of box is %0.2f"%self.barea)
        print("volume of box is %0.2f"%self.bvol)
        print("perimeter of box is %0.2f"%self.bperi)
print("enter the length,width and height:")
l=int(input())
b=int(input())
h=int(input())
b=Box(l,w,h)
b.barea_bperi_bvol()
b.disp()



        
        
        
        

class Rectangle:
	def __init__(self,width,height):
		self.height=height
		self.width=width
		
	def __gt__(self,other):
		area_self=self.height*self.width
		area_other=other.height*other.width
		if area_self>area_other:
			return True
		else:
			return False

	def __lt__(self,other):
		area_self=self.height*self.width
		area_other=other.height*other.width
		if area_self<area_other:
			return True
		else:
			return False

	def __eq__(self,other):
		area_self=self.height*self.width
		area_other=other.height*other.width
		if area_self==area_other:
			return True
		else:
			return False

print("Comparision of two rectangle objects")
h1=int(input("Enter height of rect1"))
w1=int(input("Enter width of rect1"))
h2=int(input("Enter height of rect2"))
w2=int(input("Enter width of rect2"))

rect1 = Rectangle(h1,w1)
rect2 = Rectangle(h2,w2)

print(f"Rect1>Rect2,{rect1>rect2}")
print(f"Rect1<Rect2,{rect1<rect2}")
print(f"Rect1==Rect2,{rect1==rect2}")


		
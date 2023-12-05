import random
class Myexception(Exception):
    def __init__(self,arg):
        self.msg=arg
m=random.randint(1,10)
count=0
while(count<5):
    try:
        x=int(input("enter a number:"))
        if(x>m):
            raise Myexception("sorry!!guessed no is less than entered no")
        elif(x<m):
            raise Myexception("sorry!!guessed no is greater than entered no")
        else:
            print("Wow!!you guessed the correct number")
            break
    except Myexception as me:
        print(me)
    count+=1

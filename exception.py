import random
class Myexception(Exception):
    def_init_(self,arg):
        self.msg=arg
m=random.randint(1,10)
count=0
while(count<5):
    try:
        x=int(input('enter a number')
        if(x>m):
              raise Myexception('sorry!!the guessed number is less than entered no')
            elif(x<m):
                raise Myexception('sorry!!the guessed number is more than entered no')
            else:
                print('wow!!you guessed the correct no')
                break
except Myexception as me:
    print(me)
count+=1

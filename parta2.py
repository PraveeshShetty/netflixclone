def rect():
    l=int(input('enter length:'))
    w=int(input('enter width'))
    rarea=l*w
    print('area of rectangle is:',rarea)
def circle():
    r=int(input('enter radius:'))
    carea=(22/7)*r*r
    print('area of circle is:',carea)
def square():
    s=int(input('enter the side:'))
    sarea=s*s
    print('area of square is:',sarea)
def triangle():
    b=int(input('enter base:'))
    h=int(input('enter height'))
    tarea=0.5*b*h
    print('area of triangle is:',tarea)
while(1):
    print('enter 1 for area of rectangle')
    print('enter 2 for area of circle')
    print('enter 3 for area of square')
    print('enter 4 for area of triangle')
    print('enter any number to quit')
    ch=int(input('enter your choice:'))
    if ch==1:
        rect()
    elif ch==2:
        circle()
    elif ch==3:
        square()
    elif ch==4:
        triangle()
    else:
        break
print('thank you')
    
    
    

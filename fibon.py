n=int(input("enter number of terms to print fibonacci series"))
a=0
b=1
count=0
if n<0:
    print("enter valid number:")
elif n==1:
    print("Fibonacci sequence")
    print(a)
    print(b)
while count<n:
    c=a+b
    a=b
    b=c
    count+=1
    print(c)

from array import *
a=array('i',[])
n=int(input("enter no of terms:"))
print("enter array elements:")
for i in range(n):
    a.append(int(input()))
print("array elements are:")
for i in a:
    print(i)
print("prime numbers:")
for j in a:
    if j>1:
        for k in range(2,j):
            if j%k==0:
                break
        else:
            print(j)
               

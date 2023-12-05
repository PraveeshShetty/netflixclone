t1=(1,2,5,7,9,2,4,6,8,10)
print('given tuple:',t1)
print('first half:',t1[:5])
print('second half:',t1[5:])
list1=[]
for i in t1:
    if i%2==0:
        list1+=[i]
print('even numbers:',tuple(list1))
t2=(11,13,15)
t3=t1+t2
print('tuple t1:',t1)
print('tuple t2:',t2)
print('concatinated tuple:',t3)
print('max value:',max(t3))
print('min value:',min(t3))


str=input("enter main string:")
sub=input("enter sub string:")
flag=False
pos=-1
n=len(str)
while True:
    pos=str.find(sub,pos+1,n)
    if pos==-1:
        break
    print('found at position:',pos+1)
    flag=True

if flag==False:
    print('not found')

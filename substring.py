str=input("enter main string:")
sub=input("enter sub string:")
n=str.find(sub,0,len(str))
if n==-1:
    print('sub string not found')
else:
    print('sub string found at position:',n+1)

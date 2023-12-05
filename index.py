str=input("enter main string:")
sub=input("enter sub string:")
try:
        n=str.find(sub,0,len(str))
except valueError:
    print('sub string not found')
else:
    print('sub string found at position:',n+1)

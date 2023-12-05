sen=input('enter sentence')
sen=sen.lower()
alphabet='abcdefghijklmnopqrstuvwxyz'
print('length of given sentence is:',len(sen))
dict1={}
for i in sen:
    if i in alphabet:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
print('given sentence:',sen)
print(dict1)
print('frequency of each letter')
for j in dict1:
    print(j,':',dict1[j])
                

import string
from string import digits
text=open("file.txt","r")
d=dict()
count=0

for line in text:
	line = line.strip()
	line = line.lower()
	line = line.translate(line.maketrans("","",string.punctuation))
	line = line.translate(line.maketrans("","",digits))
	words=line.split()
	count+=len(words)

	for word in words:
		if word in d:
			d[word] = d[word]+1
		else:
			d[word] = 1

print("Frequency of words")
print("*****************************************")
print("Words\tNo of occurences")
print("*****************************************")

for key in list(d.keys()):
	print(f"{key}\t\t{d[key]}")
print(f"There are total of {count} words in the file")
text.close()
	

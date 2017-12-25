import sys
import os

if (len(sys.argv)!=2):
	print "Invalid argumetnt"
	sys.exit()

if(not(os.path.exists(sys.argv[1]))):
	print "Please give the text file name: "
	sys.exit()


if (sys.argv[1].split('.')[-1]!='txt'):
	print "Please enter a text file or atleast give .txt at last of the text file DONT BE LAZY!!"
	sys.exit()


textfile=open(sys.argv[1])

dictnry={}
lst=[]


for line in textfile:
	splittedline=line.split()

	for word in splittedline:
		dictnry[word]=dictnry.get(word,0)+1
print  "\n" , dictnry, "\n"

for k,v in dictnry.items():
	lst.append((v,k))
sortedlist= sorted(lst,reverse=True)

print "Here the list of top ten words occuring maximum number of times: ", "\n"
print "    ", "Word","    ","Times"
lstnumber=[]

for i in range(10):
	wordTuple=sortedlist[i]
	lstnumber.append(len(wordTuple[1]))
	print i+1, ")" , " ",wordTuple[1],"     ",wordTuple[0]

print "Words with theri length"

print lstnumber


y=lambda x,y : x+y

average= reduce(y,lstnumber)/len(lstnumber)

print "Average of the length of the word are: " , average


square=[x**2 for x in lstnumber if x%2!=0]

print "Sqaures of the odd length word is : " , square








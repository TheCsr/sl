import sys
import os
if(len(sys.argv)!=2):
	print "Dont be lazy enter the filename.py and filename.txt in the same format!!"
	sys.exit()
if(not(os.path.exists(sys.argv[1]))):
	print "Are you a fool dont you even know that, u need to save the text file first"
	sys.exit()
if(sys.argv[1].split('.')[-1]!='txt'):
	print "Plz give the correct file dimension"
	sys.exit()
escape=open(sys.argv[1])

worddic={}
for line in escape:
	myline=line.split()
	for word in myline:
		worddic[word]=worddic.get(word,0)+1
print worddic

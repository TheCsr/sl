newlist=[]
def remove_duplicates(numbers):
	for num in numbers:
		if num not in newlist:
			newlist.append(num)
	return sorted(newlist)
a=input("Enter the no of elements: ")
l=[]

for i in range(0 , a):
	s=input("Enter list of integers:\n")
	l.append(s)
print "The entered lisst",l

print "List with removed duplicate element",remove_duplicates(l)
#print("Final list:\n",final)

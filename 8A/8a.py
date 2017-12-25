list=[]
def maximum(list):
	if len(list)==1:
		return list[0]
	else:
		m = max(list[1:])
		if m > list[0]:
			return m
		else:
			return list[0]
	
list=[10,20,25,100]
print "The max of the number is: "
print maximum(list)

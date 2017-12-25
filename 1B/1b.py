flag=1
store=[]
def ftoc(feh):
	res=((feh-32)*5)/9
	store.append(res)
	return res

def ctof(cel):
	res2=(9*cel/5)+32
	store.append(res2)
	return res2

print "Enter the choice given below:"
print " Enter 1. if u want to convert fahrenheit to celcius"
print "Enter 2, if u want to convert celcius to fahreinheit"




while flag==1:

	a=input("Enter the choice:")
	print "\n","\n"
	if a==1:
		print "Enter the Fahreinheit temperature: "
		f=input("Here:  ")
		print "The converted temp is: ",ftoc(f) , "c"
	

	elif a==2:
		print "Enter the celcius temperature: "
		c=input("Here:  ")
		print "The converted temp is: ",ctof(c), "f"
	
	print "\n", "\n"
	print "Want more conversion: ", "    " ,"y---> Yes" , "n--->no"
	check=raw_input("Enter y or n : ")
	if check=='y':
		flag=1
	else:
		flag=0

print "The list is with the last 5 conversion are :  ", store[-5:]

	


	

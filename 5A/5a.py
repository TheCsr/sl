
list=[]
a=input('Enter how many numebr you want to enter in the list: ')
for i in range(0,a):
	b=input('Here: ')
	list.append(b)
m = [x for x in list if x % 2 == 0]
print("List of even numbers:\n",m)
y=m[::-1]
print("Reversed list:\n",y)
#print(m.reverse())

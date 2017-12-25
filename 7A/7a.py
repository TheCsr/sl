class student:

	def __init__(self,usn,name,mark1,mark2,mark3):
		self.usn=usn
		self.name=name
		self.mark1=mark1
		self.mark2=mark2
		self.mark3=mark3

	def calculate(self):
		print "Total"," = ",self.mark1+self.mark2+self.mark3
	def prints(self):
		print "Name", " : ",self.name
		print "Usn", " : ",self.usn

print "The student detail are: "

s1=student("1ms15is029","Chandan",95,99,88)
s1.prints()
s1.calculate()




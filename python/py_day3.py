"""
1)
s1=raw_input("Enter string")
l1=s1.split(" ")
s2="".join(l1)
s3=" "
if s2.isalpha():
	s3=s1.title()
else:
	s3=s1
print(s3)
"""

"""
2)
n=int(raw_input("Enter the no of students : "))
i=1
s=3
student_details={}
while i<=n:
	k=raw_input("Enter name : ")
	v=[]
	j=1
	while j<=s:
		val=input("enter value for subject"+str(j)+" : ")
		v.append(val)
		j=j+1
		student_details[k]=v
	i=i+1
print(student_details)
name=raw_input("Enter name : ")
total=0
avg=0
for k in student_details.iterkeys():
	if (k==name):
		total=sum(student_details[k])
		avg=total/s;
		print(avg)
	else:
		pass
"""

"""
3)
def check(a,b):
	try:
		c=a/b
		print(c)
	except ZeroDivisionError as x:
		print "Error Code : ",x
	except ValueError as y:
		print(y)
i=0
n=input("enter no of test cases")
while i<n:
	a=raw_input("Enter a : ")
	b=raw_input("Enter b : ")
	c=str(b)
	if c.isdigit()==True:
		check(int(a),int(b))
	else:
		print("Error Code : invalid literal for int() with base 10")
	i+=1
"""

"""
4)
n=int(raw_input("Enter the no of commands : "))
i=1
l=[]
while i<=n:
	s=raw_input("Enter the command : ")
	if(s=="insert"):
		index=input("Enter index : ")
		value=input("Enter value : ")
		l.insert(index,value)
	if(s=="print"):
		print(l)
	if(s=="remove"):
		value=input("Enter the value to remove : ")
		try:
			l.remove(value)
		except Exception as err:
			print(err)
	if(s=="append"):
		value=input("Enter the value to append : ")
		l.append(value)
	if(s=="sort"):
		l.sort()
	if(s=="pop"):
		l.pop()
	if(s=="reverse"):
		l.reverse()
	i+=1
"""
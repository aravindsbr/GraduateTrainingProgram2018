"""
1)
fn=raw_input("Enter first name : ")
ln=raw_input("Enter last name : ")
print("Your Full Name : %s %s"%(fn,ln))
"""

"""
2)
name=raw_input("Enter your full name : ")
age=int(raw_input("Enter age : "))
print(name.split(" "),age)
if (age>=18):
    print("Eligible to vote")

else:
	print("Not eligible to vote")
"""

"""
3)
dob=raw_input("Enter DOB : ")
dob_list=dob.split("/")
a=[]
for i in dob_list:
	a.append(int(i))
b=sum(a)
print(b)
dob_str=str(b)
c=0
for i in dob_str:
	c+=int(i)	
print("Result is %s"%c)
"""

"""
4)
a=int(raw_input("Enter a : "))
b=int(raw_input("Enter b : "))
c=int(raw_input("Enter c : "))
sum=0
if((a==b) or (b==c) or (c==a)):
	print(sum)
else:
	print(a+b+c)
"""

"""
5)
leap=int(raw_input("Enter the year : "))
flag=0
if (leap%4==0):
	flag=1
	if(leap%100==0):
		if(leap%400==0):
			flag=1
		else:
			flag=0
if(flag==1):
	print("Leap year")
else:
	print("Not a leap year")
"""	

"""
6)
s1=raw_input("Enter a sentence : ")
lower=[]
upper=[]
for i in s1:
	if i.isupper():
		upper.append(i)
	if i.islower():
		lower.append(i)
u_len=len(upper)
l_len=len(lower)
print("UPPER CASE : %s"%u_len)
print("LOWER CASE : %s"%l_len)
"""

"""
7)
pw=raw_input("Enter password : ")
l_flag=0
u_flag=0
n_flag=0
s_flag=0

for i in pw:
	if(i.isupper()):
		u_flag+=1
	elif(i.islower()):
		l_flag+=1
	elif(i.isalnum()):
		n_flag+=1
	else:
		s_flag+=1
		
if((l_flag>=1) and (u_flag>=1) and (n_flag>=1) and (s_flag)):
	print("Password is strong")
else:
	print("Password is weak")
"""

"""
8)
a=[1,3,5,1,34,12,56]
even=[]
for i in a:
	if(i%2==0):
		even.append(i)
total=sum(even)
print("Sum of even numbers : %s"%total)
"""

"""
9)
s1=raw_input("Enter the sequence : ")
s2=s1.split(",")
print(s2)
print(tuple(s2))
"""	


	
	
	
	

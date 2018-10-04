"""
student_dict={}
student_dict["name"]="Aravind"
student_dict["Marks"]=[90,80,70]
student_dict["rollno"]=7
student_dict["Marks"]={}
student_dict["Marks"].append(50)
print(student_dict)
"""

"""
d={1:"a",2:"b",3:"c"}
for k in d.iterkeys():
	print(k)
print(d.keys())
print(d.values())
print(d.items())
print(d.viewkeys())
print(d.viewvalues())
print(d.viewitems())
"""

"""
emp={"name":"aravind","skill":["python","git","agile"]}
for k,v in emp.iteritems():
	print(k,v)
	if isinstance(v,list) :
		for a in v:
			print(a)
emp["skill"][0]="java"
print(emp)
"""			
"""
def add(a,b=5):
	#print(a,b)
	c=a+b
	return c
out=add(1,2)
print out
"""

"""
def fun(*a):
	print(a)
fun(1,2,"a",True)

def fun2(**a):
	print(a)
fun2(a=1,b=2,c="a",d=True)
"""

"""
import requests
resp=requests.get("https://www.google.com/")
if resp.status_code == 200:
	cont=resp.content
	with open ("google.html","wb") as obj:
		obj.write(cont)
"""
"""
import re
f1=open("mobile.txt","r")
f2=f1.read()
reg1=re.findall("([A-Za-z]+)\s.*\s(\$[0-9]+)",f2)
print(reg1)
f3=f1.readlines()
reg2=[]
for i in f3:
	reg2=re.findall("([A-Za-z]+)\s.*\s(\$[0-9]+)",i)
print(reg2)
"""
"""
#OR
"""
print(re.findall("([A-Za-z]+)\s.*\s(\$[0-9]+)",open("mobile.txt","r").read()))
"""

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

"""
class Sample:
	def fun1(self,a):
		return a
res=Sample().fun1(5)
print type(res)
"""
"""
class Shapes:

	def __init__(self,r,l,b=1):
		self.r=r
		self.l=l
		self.b=b
		self.circle()
		self.rect()
		
	def circle(self):
		try:
			if(self.r>0):
				area=3.14*self.r*self.r #self.r
				print area
			else:
				return "Print valid value"
		except Exception as e:
			print(e)
			
	def rect(self):
		try:
			if (self.l>0) and (self.b>0):
				area=self.l*self.b
				print area
			else:
				return "Print valid value"
		except Exception as e:
			print(e)
obj=Shapes(2,5,4)
print(id(obj))
obj=Shapes(2,5,4)
print(id(obj))
"""
"""
r=input("Enter radius : ")
c=obj.circle(r)
print(c)
l=input("Enter length : ")
b=input("Enter breadth : ")
r1=obj.rect(l,b)
print(r1)
"""
"""
import pandas as pd
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
data1 = pd.DataFrame(data=raw_data_1)
print data1
raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
data2 = pd.DataFrame(data=raw_data_2)
print data2
raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
data3 = pd.DataFrame(data=raw_data_3)
print data3
all_data = data1.append(data2)
print all_data
all_data['all_data_col']=all_data['first_name']+all_data['last_name']
print all_data
print pd.merge(all_data,data3,on='subject_id')
print pd.merge(data1,data2,on='subject_id',how='inner')
"""

"""
import pandas as pd
import csv
chipo=pd.read_csv('chipotle.tsv', sep='\t')
print(chipo)
print pd.DataFrame(chipo,columns=['item_name','item_price'])
sorted = chipo.sort_values(by='item_name')
print sorted
print chipo.max('item_price')
"""

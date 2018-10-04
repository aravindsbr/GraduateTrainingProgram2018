"""
s1=raw_input("Enter the string")
i=0
j=1
for i in s1:
	for j in s1:
		a=int(i)
		b=int(j)
		if s1[a]==s1[b]:
			print("I"+i)
			print("J"+j)
"""
"""
5)
from heapq import nlargest

name = list(raw_input("enter the name:"))
print(name)
a = {}

for i in name:
	a[i] = name.count(i)

print(a)
three_largest = nlargest(3, a, key=a.get)

for i in three_largest:
	for k,v in a.iteritems():
		if(k==i):
			print k,v
			
"""
"""
6)
cnt=input("no of test cases")
i=0
j=0
flag=0
l=[]

while i<cnt:

	d=raw_input("enter value for a:")
	a=set(d.split(" "))
	print(a)
	c=raw_input("enter value for b:")
	b=set(c.split(" "))
	print(b)

	if (a.issubset(b)==True):
		flag=1
	else:
		flag=0

	if(flag==1):
		l.append(True)
	else:
		l.append(False)

	i=i+1

for i in l:
	print(i)
"""
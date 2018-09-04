"""
# 1)
inventory = {
                   'gold' : 500,
                   'pouch' : ['flint', 'twine', 'gemstone'],
                   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
             }
# qn 1
inventory["pocket"]=[]
print(inventory)

# qn 2
inventory["pocket"]=['seashell', 'strange berry','lint']
print(inventory)

# qn 3
inventory["backpack"].sort()
print(inventory)

#qn 4
del inventory["backpack"][2]
print(inventory)

#qn 5
inventory["gold"]=[500,50]
print(inventory)
"""

"""
2)
# qn 1
#student_details={'student1':[90,85, 80],
#			 'student2':[70,80,60]}
student_details={}
n=input("Enter number of students")
s=input("Enter number of subjects")
i=1


while i<=n:
	k=input("Enter key")
	v=[]
	j=1
	while j<=s:
		val=input("enter value for subject"+str(j))
		v.append(val)
		j=j+1
		student_details[k]=v
	i=i+1

print(student_details)
# qn 2

total=0
avg=0
for a in student_details.iterkeys():
	total=str(sum(student_details[a]))
	print("Total of "+a+" is "+total)
	total=int(total)
	avg=total/len(student_details[a])
	print("Average of "+a+" is "+str(avg))
"""
	

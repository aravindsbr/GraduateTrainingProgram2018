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
student_details={'student1':[90,85, 80],
				 'student2':[70,80,60]}
print(student_details)
# qn 2
total=0
avg=0
for k in student_details.iterkeys():
	total=str(sum(student_details[k]))
	print("Total of "+k+" is "+total)
	total=int(total)
	avg=total/len(student_details[k])
	print("Average of "+k+" is "+str(avg))
"""
	
	
	

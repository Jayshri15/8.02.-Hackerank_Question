list1=["flower","flow","flight"]
list2=[]
i=0
while i<len(list1):
	if list1[0][0]==list1[1][0]==list1[2][0]and list1[0][1]==list1[1][1]==list1[2][1]:
		list2.append(list1[0][0])
		list2.append(list1[0][1])
	print(list2[0], list2[1])
	break
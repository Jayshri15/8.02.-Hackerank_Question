list1=[[3,16,2,8],[7,3,8,2],[4,6]]
list2=(list1[0])
list3=(list1[1])
list4=(list1[2])
i=0
mul=1
sum=0
var=0
while i<len(list2):
    mul*=list2[i]
    i=i+1
j=0
while j<len(list3):
    sum+=list3[j]
    j=j+1
x=0
while x<len(list4):
    var+=list4[x]
    x=x+1
print(var)
print(mul)
print(sum)



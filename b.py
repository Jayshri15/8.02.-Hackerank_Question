




keys=[]
values=[]
n=int(input("Enter the chance.."))
print("For keys:")
for x in range(0,n):
    element=int(input("Enter the value.."))
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=input("Enter the name..")
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is:    ")
print(d)








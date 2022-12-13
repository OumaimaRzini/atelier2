list=[11,45,8,11,23,45,23,45,89]
l1=list[:len(list)//3]
l2=list[len(list)//3:(len(list)//3)*2]
l3=list[(len(list)//3)*2:]

l1=l1[::-1]
l2=l2[::-1]
l2=l3[::-1]
print(l1)
print(l2)
print(l3)
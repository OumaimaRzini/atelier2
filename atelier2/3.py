list=[11,45,8,11,23,45,23,45,89]
dict={}
set1=set(list)
for i in set1:
    dict[i]=list.count(i)

print(dict)   
    
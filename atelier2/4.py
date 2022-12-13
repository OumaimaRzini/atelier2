set1={23,42,65,57,78,83,29}
set2={57,83,29,67,73,43,48}

i=set1.intersection(set2)
print(i)
for ele in i:
    set1.discard(ele)
print(set1)


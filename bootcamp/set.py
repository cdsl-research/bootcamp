set1=set([1,2,3,4,5])
print(len(set1))
print(set1)

set2=set()
set2.add(3)
set2.add(4)
set2.add(5)
set2.add(6)
set2.add(7)
set2.add(7)
print(set2)

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

#setf=frozenset(10)
#setf.add(11)


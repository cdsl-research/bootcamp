tuple1=(1,2,3,4,5)
tuple2 = tuple1+(6,7,8,9,10)
print(tuple2)
print(tuple2[0:5])

list1=[1,2,3,4,5]
list1.append(6)
list1.append(5)
print(list1)
print(list1.index(5))
print(list1.count(5))

list2=list1
list2.remove(6)
print(list2)

print(list2.pop(0))
print(list2)




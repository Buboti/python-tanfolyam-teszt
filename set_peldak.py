s1= set()
s1.add(1)
s1.add(2)
print(s1)
s2 = {4, 'alma' , 44}
print(s2)
list1 = [1, 2, 3, 1 ,2 ,3 ,4,5, 3,2 ,5 ,6,3,6, 7,5, 3,5,43,2]
list2 = list(set(list1))
print(list2)
 # print(s2[0])
s2.discard('alma')
print(s2)
s2.remove(44)
print(s2)


print(range(10))
print(range(1,10,))
print(range(-1,10,))
 # print(range(1,10,0))
print(range(1,10,2)[1])
print(range(0,1000000))
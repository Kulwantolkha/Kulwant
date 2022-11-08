#{curly bracket} are used in sets
s = set()
print(type(s))
x=set([1,2,3,4,5])
print(x)
print(type(x))
l = ['Ankit, Rahul, Yash, Ishant']
y = set(l)
print(type(l))
print(y)
#Difference between sets and list is that same element cannot be printed again in sets but in list an element can be printed multiple times
m = [4,5,6,7,8,9,4]
z = set(m)
print(z)
#To add element to an empty set
x = set()
x.add(1)
# print(x)
#Union is used to add another set in the same element Eg.(Union as used in maths)
x =  x.union({1,2,3})
print(x)
# #Similarly for intersection
x= x.intersection({1,2,4,5,6})
print(x)
# #We can add multiple sets through single print 
print(l,x)
x1= x.union({4,3,5})
print(x,x1)
# #To get the maximum or minimum output 
print(max(x))
print(min(x))
# #To remove a element form a set
print(x.remove(2))


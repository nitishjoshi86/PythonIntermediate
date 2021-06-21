#tuple: ordered, immutable, allows duplicate element

""" mytuple = tuple(['max', 28, 'boston'])
print(mytuple)

item = print(mytuple[1])

for i in mytuple:
    print(i)

if 'max' in mytuple:
    print(True)
else:
    (False)

 """

""" mytuple = ('n', 'i', 't', 'i', 's', 'h') 
print(len(mytuple))
print(mytuple.count('z'))
print(mytuple.index('t'))

mylist = list(mytuple)
print(mylist)
mytuple1 = tuple(mylist)
print(mytuple1)

 """ 

""" a = (1,2,3,4,5,6,7,8,9)
b = a[2:5:2]
print(b) """

""" newtuple = 'nitish', 34, 'delhi'
name, age, city = newtuple
print(name)
print(age)
print(city)
 """

""" q = (0,1,2,3,4)
d1, *d2, d3 = q

print(d1)
print(d2)
print(d3)
 """
""" import sys

mylist = [0,1,2,'hello',True]
mytuple = (0,1,2,'hello',True)
print(sys.getsizeof(mylist),'bytes')
print(sys.getsizeof(mytuple),'bytes') """


import timeit
print(timeit.timeit(stmt='[0,1,2,3,4,5,6,7,8,9]',number=1000000))
print(timeit.timeit(stmt='(0,1,2,3,4,5,6,7,8,9)',number=1000000))
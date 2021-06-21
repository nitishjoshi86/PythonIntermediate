#dictionary: key-value pairs, unordered, mutable

""" mydict = {'name':'nitish', 'age': 34, 'city': 'delhi'}
print(mydict) """

""" mydict1 = dict(name='joshi', age=25, city='bangalore')
print(mydict1)

value = mydict['name']
print(value)

mydict['email'] = 'nitish@gmail.com'
print(mydict)


del mydict['email']
print(mydict)
mydict.popitem()
print(mydict) """

""" if 'name' in mydict:
    print(True)
else:
    print(False)

try:
    print(mydict['name'])
except:
    print('error')

for key in mydict:
    print(key)  
for key, value in mydict.items():
    print(key, value)
 """
#copy will also change the original 
"""
mydict = {'name':'nitish', 'age': 34, 'email': 'nj@gmail.com'}
mydict1 = dict(name='joshi', age=35, city='bangalore')

mydict.update(mydict1)
print(mydict)  """

mydict={3:9,6:36,9:81}
print(mydict)
mydict1=(8,7)
mydict={mydict1:15}
print(mydict)

import json


""" person = {'name':'joshi','age':35,'city':'rajkot','haschild':False,'titles':['engineer','programmer']}
personj = json.dumps(person, indent=4,separators=('; ', ' = '), sort_keys=True)
print(personj)

with open('person.json','w') as file:
    json.dump(person,file, indent=4, sort_keys=True)
 """
""" person = json.loads(personj)
print(person) """

""" with open('person.json','r') as file:
    person = json.load(file)
    print(person) """

class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user1 = user('niti',27)

""" def encodeuser(o):
    if isinstance(o,user1):
        return {'name':o.name, 'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('user json not serializable') """
from json import JSONEncoder
class useencode(JSONEncoder):
    def default(self, o):
        if isinstance(o, user1):
            return {'name':o.name, 'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)



userjson = useencode().encode(user)
print(userjson)

def decode_user(dct):
    if user1.__name__ in dct:
        return user1(name=dct['name'],age=dct['age'])
    return dct

user = json.loads(userjson, object_hook=decode_user)
print(user.name)
import random
import secrets


a = random.randrange(1,10)
print(a)
a = random.random()
print(a)
a = random.randint(1,10)
print(a)
a = random.uniform(1,10)
print(a)
a = random.normalvariate(0,1)
print(a)
a = random.normalvariate(0,1)
print(a)

mylist = list('abcdefg')
a = random.choice(mylist)
print(a)

mylist = list('abcdefg')
a = random.sample(mylist, 3)
print(a)

mylist = list('abcdefg')
a = random.choices(mylist, k=3)
print(a)

mylist = list('abcdefg')
random.shuffle(mylist)
print(mylist)

random.seed(1)

print(random.random())
print(random.randint(1,10))

random.seed(1)

print(random.random())
print(random.randint(1,10))

random.seed(2)

print(random.random())
print(random.randint(1,10))

random.seed(3)

print(random.random())
print(random.randint(1,10))

a = secrets.randbelow(10)
print(a)

a = secrets.randbits(8)
print(a)

mylist = list('kfjnagiegrnivnkjdfgneoiunivjn')
a = secrets.choice(mylist)

print(a)

import numpy as np

a = np.random.rand(3,3)
print(a)
a = np.random.randint(0,10,3,(3,4))
print(a)


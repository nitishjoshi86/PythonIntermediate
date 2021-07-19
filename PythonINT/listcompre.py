""" lst = [1,2,3,4,5,6,7,8,9]

a = [x for x in lst]
d = [x - 1 for x in lst]
e = [x ** 2 for x in lst]
b = [x for x in lst if x > 4]
c = [x for x in lst if x % 2 == 0 and x > 4]
f = [x if x > 4 else 'less than four' for x in lst]
g = ['two' if x % 2 == 0 else 'three' if x % 3 == 0 else 'not 2 and three' for x in lst]
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g) """

""" lst = [1,2,3]
lst1 = [9,8,7]
a = [(x,y) for x in lst for y in lst1]
print(a) """


b = ['FizzBuzz' if x % 3 == 0 and  x % 5 == 0  else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, 99)]
print(str(b))

print(['FizzBuzz' if x % 3 == 0 and  x % 5 == 0  else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, 99)])
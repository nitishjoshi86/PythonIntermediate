#lambda: arguments : expression
#map: (func,sequence)




add9 = lambda x: x+9
print(add9(56))

mult = lambda x,y: x*y
print(mult(2,7))

points = [(1,2),(45,3),(9,-32),(56,-23)] 

points1 = sorted(points, key=lambda x:x[0] + x[1])
print(points)
print(points1)

a = [1,2,3,4,5]
b = map(lambda x: x%2,a)
print(list(b))

c = [x for x in a if x%2==0]

print(c)

#reduce(func, seq)

from functools import reduce

a = [1,2,3,4,5,6]

product = reduce(lambda x,y: x*y,a)
print(product)



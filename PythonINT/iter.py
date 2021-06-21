#itertools: product, permutations, combinations, accumulate, groupby and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle,repeat 
import operator


""" a = [1,2]
b = [3,4]
prod = product(a,b, repeat=2)
print(list(prod)) """

""" a = [1,2,3]
perm = permutations(a, 2)
print(list(perm)) """

""" a = [9,8,7,6]
comb=combinations(a,2)
print(list(comb))

combb = combinations_with_replacement(a,2)
print(list(combb)) """


#a = [1,2,3,4]
""" acc=accumulate(a, func=operator.mul)
print(a)
print(list(acc))
"""
""" persons = [{'name':'tim','age':25},{'name':'nitish','age':23},{'name':'lisa','age':45},{'name':'joshi','age':34}]



def smaller_than_3(x):
    return x<3

group = groupby(a,key=smaller_than_3)
for key, value in group:
    print(key, list(value))

def smaller_than_30(y):
    return y<30

group = groupby(persons,key=lambda y: y['age'])
for key, value in group:
    print(key, list(value))
 """

for i in count(10):
    print(i)

    if i ==15:
        break


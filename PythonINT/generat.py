""" def mygenerator():
    yield 9
    yield 2
    yield 7

g = mygenerator()

for i in range:
    print(g)

print(sum(g))
print(sorted(g)) """
 
""" def countdown(num):
    print('starting')
    while num>0:
        yield num
        num -= 1

cd = countdown(4)
value=next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd)) """

""" def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

#generator implement
def firstgen(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(list(firstgen(20)))
print(sum(firstgen(20)))
print(firstn(10))
print(sum(firstn(10))) """

#fibonacci: 0, 1, 1, 2, 3, 5...

""" def fibonac(limit):
    a,b = 0, 1
    while a < limit:
        yield a
        a,b = b, a+b

fib = fibonac(90)
for i in fib:
    print(i)
 """

mygen = (i for i in range(99) if i %2 == 0)

print(list(mygen))


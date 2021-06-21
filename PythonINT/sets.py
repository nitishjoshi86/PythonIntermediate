#sets: unordered, mutable, no duplicates

""" myset = set([1,2,3,4,5,6,7,8])


myset1 = set('Hello how are you')
print(sorted( myset1))

myset.add(99)
print(myset)
myset.remove(3)
print(myset.pop())
print(myset)

for i in myset:
    print(i)

if 10 in myset:
    print('yes')
else:
    print(False) """

""" o = {1,3,5,7,9}
e = {0,2,4,6,8}
p = {2,3,5,7}

u = o.union(e)
print(u)

i = o.intersection(p)
print(i)
 """
""" seta = {1,2,3,4,5,8,9}
setb = {2,3,4,9,8,6,5}

diff = seta.symmetric_difference(setb)
print(diff)

seta.update(setb)
print(seta)

seta.intersection_update(setb)
print(seta)

seta.difference_update(setb)
print(seta)

seta.symmetric_difference_update(setb)
print(seta) """

seta = {1,2,3,4}
setb = {2,3,4}

print(setb.issubset(seta))
print(seta.isdisjoint(setb))
print(seta.issuperset(setb))


setb = seta.copy()
setb.add(99)
print(seta)
print(setb)

a = frozenset([1,2,3,4])
print(a)
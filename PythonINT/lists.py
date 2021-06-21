#lists: ordered, allows duplicate elements

""" mylist = ['banana', 'cherry', 'apple']
print(mylist)
mylist.append('lemon')
print(mylist)
mylist2=[5, True, 'mango', 'mango']
mylist3=mylist2[2]
print(mylist2)
print(mylist3)

for i in mylist3:
    print(i)

if 'mango' in mylist3:
    print('yes')
else:
    print('no')

print(len(mylist2))

mylist.insert(1,'peaches')
print(mylist)
mylist.pop()
print(mylist)
mylist.remove('peaches')
print(mylist)
mylist.reverse()
print(mylist) """

mylist = [4,-9,2,1,99,0,-1,-2,-3,-4,12]
print(mylist)
mylist1=sorted(mylist)
print(mylist1)

list1 = [0]*5
print(list1)

a = [1,2,3,4,5,6,7,8,9]

b = print(a[1::2])

original = ['banana','cherry','mango']
ori=original
ori.append('lemon')
print(ori)
d=[2,23,345,345,65,4,7]
c=[i*i for i in d]
print(c)



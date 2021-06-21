""" def fab(a, b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
fab(1,2,3,4,5,6, six = 6, seven = 7)
 """

""" def fab(a, b, c):
    print(a, b, c)

mylist = [1, 2, 3] #list or tuple, length of the container must match number of parameters

fab(*mylist)
"""


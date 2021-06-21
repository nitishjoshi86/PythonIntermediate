#exception: errors & exceptions

""" x = -5
assert (x>=0), 'x is not positive'
if x <0:
    raise Exception('x should be more than 0')
 """
""" from typing import final


try:
    a = 5/0
    b = a+'10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('clear operation') """



class valuehigh(Exception):
    pass

class valuesmall(Exception):
    def __init__(self, message, value): 
        self.message = message
        self.value = value

def testvalue(x):
    if x>100:
        raise valuehigh('not valid marks')
    elif x<0:
        raise valuesmall('not valid marks too small',x)

try:
    testvalue(-200)
except valuehigh as e:
    print (e)
except valuesmall as e:
    print(e.message, e.value)

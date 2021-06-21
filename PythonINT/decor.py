""" def start_deco(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@start_deco
def printname():
    print('joshi')

#printname = start_deco(printname)
printname() """

""" def start_deco(func):

    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('end')
        return result
    return wrapper

@start_deco
def add9(x):
    return x+9

#printname = start_deco(printname)
result = add9(10)
print(result)
print(help(add9))
print(add9.__name__) """

 
import functools

def repeat(num_times):
    def decor_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decor_repeat
 


def greet(name):
    print(f'hello {name}')
    print(greet)
    return greet

greet('alex') 
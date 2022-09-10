import datetime
file = open('new.txt','w+')
file.write("Function name     |     Worked time     |     Arguments as List     |     Arguments as dictionary     |     Results\n")

def logger(func):
    def wrapper(*args,**kwargs):
        try:
            result = func(*args,**kwargs)
        except ZeroDivisionError as err:
            result = err
        file.write(f'{func.__name__}             |     { datetime.datetime.now()}      |   {args}      |      {kwargs}      |      {result}\n')

        return result
    return wrapper
@logger
def sum(a,b):
    return a+b

@logger
def divide(a,b):
    return a/b



sum(1,2)
divide(a=4,b=2)
divide(10,0)
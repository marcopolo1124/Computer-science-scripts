def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
   print('display function ran')

@decorator_function
def say_hi(name):
    print('Hi, ' +name )

say_hi('Marco')
display()



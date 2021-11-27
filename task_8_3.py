def print_value(func):
    def wrapper(*args, **kwargs):
        print(f"Call for: {func.__name__}")
        print(f"{args}: {type(args)}")
        rez = func(*args, **kwargs)
        print(f"Rezult: {rez} type: {type(rez)}")
        return rez
    return wrapper

@print_value
def calc_cube(x):
   return x**3


calc_cube(3)

"""
5: <class 'int'>
Rezult: 125  type: <class 'int'>
"""
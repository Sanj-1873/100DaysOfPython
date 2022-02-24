# * --> many positional arguments, collects them into a tuple,
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add( 3,4,2,132))

# ** many keyword arguments, collects them into a dict 

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


def add(a, b):
    try:
        return a+b
    except:
        raise TypeError

def multiply(a, b):
    try:
        return a*b
    except:
        raise TypeError

 def sub(a, b):
    try:
        return a-b
    except:
        raise TypeError

def divide(a, b):
    try:
        return a/b
    except:
        raise TypeError

def power(a, b):
    assert type(b) is int
    if b == 1:
        return a
    else:
        return a*power(a, b-1)
        
def factorial(a):
    assert type(a) is int
    assert a>=0:
    if a == 1 or a == 0:
        return a
    else:
        return a*factorial(a-1)

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

def factorial(a):
    assert type(a) is int
    if a == 1:
        return a
    else:
        return a*factorial(a-1)
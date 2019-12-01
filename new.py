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
def addition(a,b):
    return a+b

def substract(a,b):
    return a-b

def division(a,b):
    try:
        result = a/b
    except:
        result = "Division is not possible as zero is being used in denominator"
    return result

def multiply(a,b):
    return a*b
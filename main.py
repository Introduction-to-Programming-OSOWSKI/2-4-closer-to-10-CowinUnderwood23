#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    
   
    
    if abs(10 - x) > abs(10 - y):
        return y

    elif abs(10 - y) == abs(10 - x):
        return 0

    else:
        return x

print(close10(5, -10))

    
print(abs(-5 + 4 * 100))

def function(x):
    if x % 10 == 0:
        return True

    else:
        return False


def functions(x, y, z):
    if x > 10 and (y > 10 or z == 5):
        return True
    
    else:
        return False

print(functions(12, 15, 5))

# My solution
def is_triangle(a, b, c):
    if (a < b+c) and (b < a+c) and (c < a+b):
        return True
    else:
        return False

# Clever solution
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

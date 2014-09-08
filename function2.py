def a(x, y, z):
    if x:
        return y
    else:
        return z

def b(q, r):
    return a(q>r, q, r)
    
    
    
a(3>2, a, b)
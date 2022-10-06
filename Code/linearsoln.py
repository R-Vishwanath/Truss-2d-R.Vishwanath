import numpy as np
def linear_solve(q,b):
    a=np.array(q)
    b=np.array(b)
    c=np.linalg.solve(a,b)
    return(c)

def lstsqr_(q,b):
    a=np.array(q)
    b=np.array(b)
    c=np.linalg.lstsq(q,b)

    return c
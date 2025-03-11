"""Implement backward substitution algorithm"""

import numpy as np

def BackwardSubstitution(A, b, y=None):
    if y is None:
        y=np.zeros(len(b), dtype=float)
    
    n=len(A)  
    if n==1:
        y[0]=b[0]/A[0,0]
        return y
    
    y[-1]=b[-1]/A[-1, -1]
    b1=b[:-1]-y[-1]*A[:-1, -1]
    y[:-1]=BackwardSubstitution(A[:-1, :-1], b1, y[:-1])
    
    return y

if __name__ == "__main__":
    A = np.array([[1, 2, 3], [0, 1, 0], [0, 0, 2]])             
    b = np.array([8, 1, 4])

    y_sol = BackwardSubstitution(A, b)
    print("y_sol:", y_sol)
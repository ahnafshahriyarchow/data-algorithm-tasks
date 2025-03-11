"""Implement a variant of vanilla gradient descent algorithm to minimize the function
f(x1,x2)=(1/3)*x1**3 + x2**2 + 2*x1*x2-6 * x1-3 * x2 - cos(pi*x1)+4
In the implementation, modify this algorithm by adding an iteration limit, so that if the iteration limit is
reached, then the algorithm outputs the best solution found"""

import numpy as np

def f(x):
    x1,x2=x
    return (1/3)*x1**3 + x2**2 + 2*x1*x2-6 * x1-3 * x2-np.cos(np.pi*x1)+4

def grad_f(x):
    x1,x2=x
    df_dx1=x1**2+2*x2-6+np.pi*np.sin(np.pi*x1)
    df_dx2 = 2 * x2 + 2 * x1 - 3
    return np.array([df_dx1, df_dx2])

def gradient_descent_algorithm(fx, x0, deps=0.001, eta=0.1, iter_lim=1000):
    x=np.array(x0, dtype=float)
    best_x=x.copy()
    best_fx=f(x)
    n_iter=0
    
    while np.linalg.norm(grad_f(x))>=deps and n_iter<iter_lim:
        x=x-eta*grad_f(x)
        fx=f(x)
        if fx<best_fx:
            best_x=x.copy()
            best_fx=fx
        n_iter+=1
    
    return n_iter, best_x, best_fx

if __name__ == "__main__":
    x0=[0, -1]
    eta1=0.1
    eta2=0.2

    n_iter1, best_x1, best_fx1 = gradient_descent_algorithm(f, x0, deps=0.001, eta=eta1, iter_lim=1000)
    print(f"n_iter: {n_iter1}, best_x: [{best_x1[0]:.2f}, {best_x1[1]:.2f}], best_fx: {best_fx1:.2f}")

    n_iter2, best_x2, best_fx2 = gradient_descent_algorithm(f, x0, deps=0.001, eta=eta2, iter_lim=1000)
    print(f"n_iter: {n_iter2}, best_x: [{best_x2[0]:.2f}, {best_x2[1]:.2f}], best_fx: {best_fx2:.2f}")
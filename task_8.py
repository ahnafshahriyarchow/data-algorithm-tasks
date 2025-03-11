"""Determinant calculations can be done more efficiently by using matrix decomposition. For a given
matrix A and a PLU decomposition of it (i.e., A = PLU), we have the following:

                         det(A) = det(P) * det(L) * det(U) (1)

These individual determinants associated with P, L and U matrices are easy to calculate:
* The determinant of a triangular matrix is the product of its diagonal elements.
* Swapping two rows of a matrix multiplies the determinant by -1. Since a permutation matrix P is
obtained by swapping rows of an identity matrix (whose determinant is 1), the determinant of P
can be computed by counting how many row swaps it takes to transform an identity matrix to P,
say k. That is, det(P) = (-1)**k

Implement a python function that computes the determinant first using numpy library function linalg.det(),
then does the same using the above decomposition based approach, and returns the corresponding run
times."""



import numpy as np
from scipy import linalg
import time

def count_permutation_swaps(P):
    n = len(P)
    perm = list(np.argmax(P, axis=1))
    swaps = 0

    for i in range(n):
        while i != perm[i]:
            j = perm[i]
            perm[i], perm[j] = perm[j], perm[i]
            swaps += 1
            
    return swaps

def calc_triangular_determinant(matrix):
    return np.prod(np.diag(matrix))

def determinant_calculation_comparison(A):
 
    start_time = time.perf_counter()
    det_np = np.linalg.det(A)
    np_time = time.perf_counter() - start_time
    P, L, U = linalg.lu(A)
    start_time = time.perf_counter()
    k = count_permutation_swaps(P)
    det_p = (-1) ** k
    det_l = calc_triangular_determinant(L)
    det_u = calc_triangular_determinant(U)
    det_plu = det_p * det_l * det_u
    plu_time = time.perf_counter() - start_time
    
    return det_np, np_time, det_plu, plu_time

if __name__ == "__main__":
    A = np.array([[2, 5, 8, 7], 
                  [5, 2, 2, 8], 
                  [7, 5, 6, 6], 
                  [5, 4, 4, 8]])

    det_np, np_time, det_plu, plu_time = determinant_calculation_comparison(A)
    print(f"det_np: {det_np:.2f}, np_time {np_time:.6f}, det_plu: {det_plu:.2f}, plu_time: {plu_time:.6f}")
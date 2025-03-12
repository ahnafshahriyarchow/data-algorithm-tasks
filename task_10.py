"""We know that symmetric positive definite (SPD) matrix A can be factorized into
A = L^T * L

We are interested in the time it takes to find the lower triangular matrix that will satisfy the condition
A = L^T * L. The task is to apply Cholesky factorization using two different methods. First method is to
implement your own Cholesky factorization algorithm, and the second method is to use
numpy.linalg.cholesky() function. Compare the performances (i.e. CPU run times) of these two methods on
n randomly generated instances of varying sizes. """


import numpy as np  
import pandas as pd
import time

matrix_size = 1000
np.random.seed(1) 
AA = np.around(np.random.rand(matrix_size, matrix_size) * 10, 1)
BB = np.dot(AA, AA.transpose())

dic_instances = {100: 1, 500: 1, 1000: 1}

def run_cholesky_all(instance_sizes):
    results = []
    id_counter = 1
    for size, repetitions in instance_sizes.items():
        for _ in range(repetitions):
            A = BB[:size, :size]

            time_start = time.time()
            custom_L = custom_cholesky(A)
            cholesky_cpu_time = time.time() - time_start
            cholesky_mean_L = np.mean(custom_L[custom_L != 0])
        
            start_time = time.time()
            L_numpy = np.linalg.cholesky(A)
            np_cpu_time = time.time() - start_time
            np_mean_L = np.mean(L_numpy[L_numpy != 0])
            results.append({
                "ID": id_counter,
                "size": size,
                "cholesky_mean_L": cholesky_mean_L,
                "cholesky_CPU": cholesky_cpu_time,
                "np_mean_L": np_mean_L,
                "np_CPU": np_cpu_time
            })
            id_counter += 1
    return pd.DataFrame(results)

def custom_cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :j] ** 2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    return L

if __name__ == "__main__":
    df_cholesky_results = run_cholesky_all(dic_instances)
    print(df_cholesky_results[['ID', 'size', 'cholesky_mean_L', 'cholesky_CPU', 'np_mean_L', 'np_CPU']].to_string(index=False, float_format='%.4f'))

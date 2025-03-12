""" Consider the binary knapsack problem that can be formulated as a binary integer where W is the knapsack capacity, v = [v1,..., vn] is a vector representing the values of the items and
w = [w1,...,wn] is a vector representing the weights of the items. The task is to solve KNAPSACK by using a simulated annealing (SA) algorithm"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple

def get_initial_solution(weights: np.ndarray, values: np.ndarray, capacity: int) -> np.ndarray:
    n = len(weights)
    ratios = values / weights
    indices = np.argsort(-ratios)  
    
    solution = np.zeros(n, dtype=int)
    total_weight = 0
    
    for idx in indices:
        if total_weight + weights[idx] <= capacity:
            solution[idx] = 1
            total_weight += weights[idx]
    
    return solution

def create_neighbor(solution: np.ndarray, weights: np.ndarray, capacity: int) -> np.ndarray:
    n = len(solution)
    neighbor = solution.copy()
    
    ones = np.where(neighbor == 1)[0]
    zeros = np.where(neighbor == 0)[0]
    
    if len(ones) >= 2 and len(zeros) >= 2:
        swap_ones = np.random.choice(ones, 2, replace=False)
        swap_zeros = np.random.choice(zeros, 2, replace=False)
        
        neighbor[swap_ones] = 0
        neighbor[swap_zeros] = 1
    
    total_weight = np.sum(weights * neighbor)
    while total_weight > capacity and np.sum(neighbor) > 0:
        selected = np.where(neighbor == 1)[0]
        remove_idx = np.random.choice(selected)
        neighbor[remove_idx] = 0
        total_weight = np.sum(weights * neighbor)
    
    return neighbor

def calculate_value(solution: np.ndarray, values: np.ndarray) -> float:
    return np.sum(values * solution)

def reduce_temperature(initial_temp: float, iteration: int) -> float:
    return initial_temp / (1 + np.log(1 + iteration))

def simulated_annealing(weights: np.ndarray, values: np.ndarray, capacity: int, 
                       num_iter: int = 1000) -> np.ndarray:

    T0 = 1000 
    T = T0
    
    x_best = get_initial_solution(weights, values, capacity)
    best_value = calculate_value(x_best, values)
    
    for k in range(1, num_iter + 1):
        x_new = create_neighbor(x_best, weights, capacity)
        new_value = calculate_value(x_new, values)
        
        if new_value >= best_value:
            x_best = x_new
            best_value = new_value
        else:
            delta = new_value - best_value
            r = np.random.random()
            if r < np.exp(-abs(delta) / T):
                x_best = x_new
                best_value = new_value
        
        T = reduce_temperature(T0, k)
    
    return x_best

def solve_knapsack_dp(values: np.ndarray, weights: np.ndarray, capacity: int) -> int:
    n = len(values)
    dp = np.zeros((n + 1, capacity + 1), dtype=int)
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i,w] = max(dp[i-1,w], 
                            dp[i-1,w-weights[i-1]] + values[i-1])
            else:
                dp[i,w] = dp[i-1,w]
    
    return dp[n,capacity]

def generate_instance(n_items: int) -> Tuple[np.ndarray, np.ndarray, int]:
    values = np.random.randint(1, 20, size=n_items)
    weights = np.random.randint(1, 10, size=n_items)
    sample_soln = np.random.binomial(1, 0.25, size=n_items)
    total_weight = np.sum(sample_soln * weights)
    
    return values, weights, total_weight

def run_Knapsack_SA_all(dic_instances: Dict[int, int]) -> pd.DataFrame:
    results = []
    instance_id = 1
    
    for n_items, num_instances in dic_instances.items():
        for _ in range(num_instances):
            values, weights, capacity = generate_instance(n_items)
            
            sa_solution = simulated_annealing(weights, values, capacity, num_iter=max(100, n_items))
            sa_value = calculate_value(sa_solution, values)
            
            opt_value = solve_knapsack_dp(values, weights, capacity)
            
            gap = ((opt_value - sa_value) / opt_value) * 100 if opt_value > 0 else 0
            
            results.append({
                'ID': instance_id,
                'n_items': n_items,
                'SA': sa_value,
                'Opt': opt_value,
                'Gap': round(gap, 1)
            })
            
            instance_id += 1
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    dic_instances = {100: 1, 500: 1, 1000: 1}
    results_df = run_Knapsack_SA_all(dic_instances)
    print(results_df.to_string(index=False))
"""Implement a dynamic programming-based approach for this problem. You can construct the DP recursion using Opt(k,i),
which corresponds using color i for node k by taking into account all the nodes {0,..., k}."""

import numpy as np

def min_cost_vertex_coloring_DP(costs):
    no_of_vertices = len(costs)  
    no_of_colors = 3  

    dp = np.full((no_of_vertices, no_of_colors), float('inf'))

    for c in range(no_of_colors):
        dp[0][c] = costs[0][c]

    for k in range(1, no_of_vertices):
        for c in range(no_of_colors):
            for c_prime in range(no_of_colors):
                if c_prime != c:
                    dp[k][c] = min(dp[k][c], dp[k-1][c_prime] + costs[k][c])

    min_cost = min(dp[no_of_vertices-1])
    
    best_coloring = [0] * no_of_vertices
    last_color = int(np.argmin(dp[no_of_vertices-1]))  
    best_coloring[no_of_vertices-1] = last_color

    for k in range(no_of_vertices-2, -1, -1):
        for c_prime in range(no_of_colors):
            if c_prime != best_coloring[k+1] and dp[k][c_prime] + costs[k+1][best_coloring[k+1]] == dp[k+1][best_coloring[k+1]]:
                best_coloring[k] = c_prime
                break

    return min_cost, best_coloring, dp

costs = [[18, 3, 18], [14, 14, 4], [15, 3, 17]]
min_cost_dp, best_coloring_dp, dp_table = min_cost_vertex_coloring_DP(costs)
print(f"min_cost_dp: {min_cost_dp}")  
print(f"best_coloring_dp: {best_coloring_dp}")  
print("DP Table:")
for row in dp_table:
    print(row) 
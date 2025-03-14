"""Implement a dynamic programming-based approach for this problem. You can construct the DP recursion using Opt(k,i),
which corresponds using color i for node k by taking into account all the nodes {0,..., k}."""

import numpy as np

def min_cost_vertex_coloring_DP(costs):
    no_of_vertices = len(costs)  
    no_of_colors = 3  
    
    #initialize table with 'inf' to store the minimum cost up to each vertex
    dp = np.full((no_of_vertices, no_of_colors), float('inf'))
    
    #fill the first row of the table with the costs of coloring the first vertex
    for c in range(no_of_colors):
        dp[0][c] = costs[0][c]
        
    #fill the table iteratively
    for k in range(1, no_of_vertices):
        for c in range(no_of_colors):
            for c_prime in range(no_of_colors):
                if c_prime != c:
                    dp[k][c] = min(dp[k][c], dp[k-1][c_prime] + costs[k][c])
                    
    #find the minimum cost in the last row of the DP table
    min_cost = min(dp[no_of_vertices-1])
    
    #backtracking to find the optimal coloring configuration
    best_coloring = [0] * no_of_vertices
    last_color = int(np.argmin(dp[no_of_vertices-1]))  
    best_coloring[no_of_vertices-1] = last_color
    
    #trace back to determine the best color for each previous vertex
    for k in range(no_of_vertices-2, -1, -1):
        for c_prime in range(no_of_colors): # Check all possible colors for the previous vertex
            if c_prime != best_coloring[k+1] and dp[k][c_prime] + costs[k+1][best_coloring[k+1]] == dp[k+1][best_coloring[k+1]]:
                best_coloring[k] = c_prime
                break

    return min_cost, best_coloring, dp
    
#Test case
costs = [[18, 3, 18], [14, 14, 4], [15, 3, 17]]
min_cost_dp, best_coloring_dp, dp_table = min_cost_vertex_coloring_DP(costs)
print(f"min_cost_dp: {min_cost_dp}")  
print(f"best_coloring_dp: {best_coloring_dp}")  
print("DP Table:")
for row in dp_table:
    print(row) 

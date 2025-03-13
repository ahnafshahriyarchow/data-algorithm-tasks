"""Consider the problem of minimum cost 3-coloring of the line graphs. Note that, in line graphs, nodes are ordered on a line and there can be edges only between two adjacent
nodes. In a valid coloring, no adjacent nodes can have the same color. Implement an enumeration-based approach for this problem, which involves enumerating all the feasible combinations,
calculating the cost associated with each combination, and outputting the minimum cost combination"""

import itertools

def min_cost_vertex_coloring_enumeration(costs):
    no_of_vertices = len(costs)
    best_coloring = None
    min_cost = float('inf')  #min cost initialized with infinity 
    
    #generate all possible color combinations (each vertex can be colored with 0, 1, or 2)
    color_combinations = itertools.product([0, 1, 2], repeat=no_of_vertices)
    
    #iterate over all possible colors combinations
    for color in color_combinations:
        valid = True
        
        #check if adjacent vertices have different colors
        for i in range(1, no_of_vertices):
            if color[i] == color[i - 1]:
                valid = False
                break
        
        if valid:
            # calculate total cost for this valid coloring
            cost = sum(costs[i][color[i]] for i in range(no_of_vertices))
            
            #update minimum cost and best coloring if this configuration is better
            if cost < min_cost:
                min_cost = cost
                best_coloring = color
    
    return min_cost, list(best_coloring)

#Test case
costs = [[18, 3, 18], [14, 14, 4], [15, 3, 17]]
min_cost_enum, best_coloring_enum = min_cost_vertex_coloring_enumeration(costs)
print(f"min_cost_enum: {min_cost_enum}") 
print(f"best_coloring_enum: {(best_coloring_enum)}")

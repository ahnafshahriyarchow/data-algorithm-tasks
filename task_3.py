"""Minimum node-cover problem can be described as, given an undirected graph G = (V,E), finding
the smallest subset S ⊆ V such that each edge in E is incident to at least one node of S. Devise a greedy algorithm to find the
node cover for any given undirected graph. You can assume that you will be given only the adjacency matrix corresponding to
an undirected graph, which shows whether there is an edge between any two nodes in the graph. Since this is a greedy algorithm, it may not generate the optimum (i.e., minimum-sized) node-cover, however, any
generated solution by the greedy algorithm is still expected to be a node-cover."""

def GetNodeCover_greedy(adj_matrix):
    n=len(adj_matrix)  
    nodes_covered=set()  
    edges=set()  
    
    #extracting all edges from the matrix
    for i in range(n):
        for j in range(i+1,n):  #consider only upper triangle to avoid duplicate edges
            if adj_matrix[i][j] == 1:
                edges.add((i,j))

    #greedy approach by selecting edges and add their endpoints to the cover
    while edges:
        edge=edges.pop()   #select a random edge from the set
        u,v=edge          #extract the two nodes connected by that randomly selected edge
        nodes_covered.add(u)
        nodes_covered.add(v)

        #remove all edges that are now covered by either u or v
        edges={e for e in edges if u not in e and v not in e}
        
    return list(nodes_covered)

#Test case
np_adjacent=[
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]]

list_nodes=GetNodeCover_greedy(np_adjacent)
print("Node cover solution:", list_nodes)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

def bfs(source, sink, parent, residual_graph, num_vertices):
    # Standard BFS to find an augmenting path from source to sink
    visited = [False] * num_vertices
    queue = deque([source])
    visited[source] = True
    
    while queue:
        curr = queue.popleft()
        
        for neighbor in range(num_vertices):
            # Path exists if neighbor is not visited and residual capacity > 0
            if not visited[neighbor] and residual_graph[curr][neighbor] > 0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = curr
                if neighbor == sink:
                    return True
                    
    return False

def ford_fulkerson():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    V = int(input_data[0])
    E = int(input_data[1])
    
    # Initialize the residual graph with 0 capacities
    residual_graph = [[0] * V for _ in range(V)]
    
    idx = 2
    for _ in range(E):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        capacity = int(input_data[idx+2])
        residual_graph[u][v] += capacity  # Handles duplicate edges by summing capacities
        idx += 3
        
    source = 0
    sink = V - 1
    
    parent = [-1] * V
    max_flow = 0
    
    # Augment the flow while a path from source to sink exists
    while bfs(source, sink, parent, residual_graph, V):
        # Find the maximum flow through the path found by BFS
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
            
        # Update residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
            
        max_flow += path_flow

    print(max_flow)

if __name__ == '__main__':
    ford_fulkerson()

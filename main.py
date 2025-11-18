from collections import deque
from heapq import heappush, heappop
import math

def shortest_shortest_path(graph, source):
    """
    a) Design an algorithm to find the shortest path from s to all other vertices with the fewest number of edges.
    
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges).
    """
    
    
    # Initialize distances to (infinity, infinity)
    dist = {v: (float('inf'), float('inf')) for v in graph}
    dist[source] = (0, 0)
    
    # Priority Queue: Stores tuples of (weight, edges, vertex).
    pq = [(0, 0, source)]
    
    while pq:
        w, e, u = heappop(pq)
        
        
        if (w, e) > dist[u]:
            continue
            
        # graph returns a set of (neighbor, weight) tuples
        for v, weight in graph.get(u, set()):
            # Calculate the new path's cost
            new_w = w + weight
            new_e = e + 1
            new_dist = (new_w, new_e)
            
            # if new path is better
            if new_dist < dist[v]:
                dist[v] = new_dist
                heappush(pq, (new_w, new_e, v))
                
    return dist


def bfs_path(graph, source):
    """
    2a) Runs Breadth-First Search and returns the parent dict to track the shortest path tree.

    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parent = {source: None} # Stores parent pointers
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        
        # Iterate over the unweighted neighbors
        for v in graph.get(u, set()):
            # Check if the neighbr has been visited yet
            if v not in parent:
                parent[v] = u
                queue.append(v)
                
    return parent

    
def get_sample_graph():
     
     return {'s': {'a', 'b'},
             'a': {'b'},
             'b': {'c'},
             'c': {'a', 'd'},
             'd': {}
             }


def get_path(parents, destination):
    """
    2b) Reconstructs the shortest path from the source node to the destination node.

    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself) as a string.
    """
    path_list = []
    current_node = destination
    
    # Backtrack until the root node
    while parents.get(current_node) is not None:
        parent = parents[current_node]
        path_list.append(parent)
        current_node = parent
        
    # The path list is currently in reverse order.
    path_list.reverse()
    
    # Join with NO space
    return ''.join(path_list)

def closest_node(Q, dist):
    min_dist = float("inf")
    winning_node = None
    for u in Q:
        if dist[u] <= min_dist:
            min_dist = dist[u]
            winning_node = u
    return winning_node

def dijkstra(graph, source):
    #graph is a dictionary whose keys are nodes and whose values are
    #dictionaries containing nodes with edges to the key and lengths
    #of those edges
    Q = set() #vertex set
    dist = dict()
    prev = dict()
    for v in graph:
        dist[v] = float("inf")
        prev[v] = None
        Q.add(v)
    dist[source] = 0
    while len(Q) > 0:
        u = closest_node(Q, dist)
        print("processing " + str(u))
        Q.remove(u)
        for neighbor in graph[u]:
            alt = dist[u] + graph[u][neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u
    return (dist, prev)

def dag_dijkstra_longest(graph, destination, vertices):
    #directed acyclic graph, find longest path
    #for now, we assume the graph is in a topological ordering in vertices
    #we also assume the source is the 1 node, and it's value is stored in
    #graph[0]
    dist = dict()
    prev = dict()
    for v in vertices:
        dist[v] = -float("inf")
        prev[v] = None
    dist[1] = 0
    for vertex in vertices:
        for neighbor in graph[vertex]:
            alt = dist[vertex] + graph[vertex][neighbor]
            if alt > dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = vertex
    length = dist[destination] + graph[0]
    return (length, prev)
                
                

test_graph = {1 : {2:1, 3:2, 4:10}, 2 : {1:1, 4:5}, 3 : {1:2, 4:3}, \
              4 : {1:10, 2:5, 3:3}}

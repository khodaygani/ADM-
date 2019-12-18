import utils
# getting the data...
utils.prepare_data()
vertices,distances=utils.get_distance_graph()
vertices,times=utils.get_time_graph()

# two simple functions to get, from the data, the neigh of a node and the distance between two nodes
def get_neigh(graph,node):
    neigh=[]
    for i in range(len(graph[node])):
        neigh.append(graph[node][i][0])
    return neigh

def get_dist(graph,node1,node2):
    dist=0
    for i in graph[node1]:
        if i[0]==node2:
            dist=dist+i[1]
        else:
            dist
    return dist


# this the functionality 1
# every time you try to run the functionality you have to define the empty list below
# here i store all the nodes visited
visited = []

# while here i put the node stored and its distance from the start_node
dist = {}


# given a start_node, a graph, and a threshold...
def functionality_1(node_id, graph, d):
    # ...if the threshold its not exceeded i add the node to the ones already visited.
    if d > 0 and node_id not in visited:
        visited.append(node_id)

        # for each node i get its neigh and if they are not in 'visited' i store them...
        for i in get_neigh(graph, node_id):
            if i not in visited:
                # ...and i add the key and its values (which are the difference between the previous threshold and
                # the distance between node and one of its neigh) to the dictionary
                dist[i] = d - get_dist(graph, node_id, i)

                # and i repeate it recursively
                functionality_1(i, graph, dist[i])
    return visited


# getting all the path that can be reached from the start-node at distance equal to d (threshold)
# first of all i build a graph in order to work on it...
distance = nx.Graph()
for i in distances:
    for j in distances[i]:
        # ...adding nodes...
        distance.add_node(i)

        # ...the edges and the distance between the nodes in the edge.
        distance.add_edge(i, j[0], weight=j[1])


# simple function to get the distance of a path (given as a list of nodes)
def get_distance_path(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        if i != path[0]:
            distance += graph.edges[(path[i], path[i + 1])]['weight']
    return distance


# now i can get all the path whose distance is under the threshold
def get_path_underd(node_id, graph, dist, d):
    # take all the nodes under the threshold...
    nodes_at_d = functionality_1(node_id, dist, d)

    # ...defining a list where i store all the paths.
    paths = []
    for i in nodes_at_d:

        # for each of the nodes at distance 'd' i take the path between it and the start_node
        for j in list(nx.shortest_simple_paths(distance, node_id, i)):
            if get_distance_path(graph, j) <= d and i != node_id:
                paths.append(j)
    return paths
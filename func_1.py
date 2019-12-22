import utils
# getting the data...
utils.prepare_data()
from utils import get_neigh
from utils import d
from utils import t
from utils import get_distance_path
from utils import get_path_underd

# this the functionality 1
# every time you try to run the functionality you have to define the empty list below
# here i store all the nodes visited
visited = []

# while here i put the node stored and its distance from the start_node
dist = {}

graph = utils.get_distance_graph()
# given a start_node, a graph, and a threshold...
def functionality_1(node_id, d):
    # ...if the threshold its not exceeded i add the node to the ones already visited.
    if d > 0 and node_id not in visited:
        visited.append(node_id)

        # for each node i get its neigh and if they are not in 'visited' i store them...
        for i in get_neigh(graph, node_id):
            if i not in visited:
                # ...and i add the key and its values (which are the difference between the previous threshold and
                # the distance between node and one of its neigh) to the dictionary
                dist[i] = d - dist_func(node_id, i)

                # and i repeate it recursively
                functionality_1(i, dist_func, dist[i])
    return visited

# final functionality to take all the nodes at distance d and its 'visualisation'
def functionality(node_id,d):
    visited = []
    dist = {}
    vertices,graph = utils.get_distance_graph()
    node_at_dist = functionality_1(node_id,d)
    
    # getting all the path that can be reached from the start-node at distance equal to d (threshold)
    # first of all i build a graph in order to work on it...
    distance = nx.Graph()
    for i in distances:
        for j in distances[i]:
        # ...adding nodes...
            distance.add_node(i)

            # ...the edges and the distance between the nodes in the edge.
            distance.add_edge(i, j[0], weight=j[1])
    path = get_path_underd(node_id,distance,distances,d)
    return node_at_dist,path,vertices

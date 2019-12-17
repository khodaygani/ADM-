from utils import get_distance_graph
from utils import find_the_path

def functionality(starting_node, nodes_to_visit):
    vertices, edges = get_distance_graph()  # we get distance information.

    # finding out the best path for visit all the nodes in order.
    best_path = find_the_path(edges, starting_node, nodes_to_visit)

    return best_path  # than we return the best path
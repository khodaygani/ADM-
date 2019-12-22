from utils import get_distance_graph
from utils import find_the_path

import numpy as np


def functionality(starting_node, nodes_to_visit):
    vertices, edges = get_distance_graph()  # we get distance information.

    # first we find the best order in which we can visit the nodes
    ordered_nodes = __find_order(starting_node, nodes_to_visit, vertices)

    # than the best path to visit them
    best_path = find_the_path(edges, starting_node, ordered_nodes)

    return vertices, best_path  # than we return the best path


def __find_order(start, to_visit, coordinates):
    to_visit_list = list(to_visit)  # iterate on a list is faster than do that on a set.
    ordered_path = []  # defining as empty the list that will maintain the order in in which we will visit the nodes.

    while to_visit_list:

        # initialise the min dist.
        min_dist = __get_real_dist(start, to_visit_list[0], coordinates)
        nearest_node = to_visit_list[0]

        for node in to_visit_list:  # try to find a smaller dist, so a closer node
            if min_dist > __get_real_dist(start, node, coordinates):  # check if is nearer than the one found before:
                min_dist = __get_real_dist(start, node, coordinates)  # if it is, update the distance
                nearest_node = node  # and elect it as nearer node.

        # once found:
        to_visit_list.remove(nearest_node)  # removed from the list of nodes to visit
        start = nearest_node  # elect it as starting node for the new iteration
        ordered_path.append(nearest_node)  # and appending it as first node to visit in the ordered path

    return ordered_path  # returning the result.


def __get_real_dist(node1, node2, coordinates):  # using the euclidean distance for calculate the distance between nodes
    return np.linalg.norm(np.array(coordinates[node1]) - np.array(coordinates[node2]))




from utils import get_distance_graph
import numpy as np


def functionality(starting_node, nodes_to_visit):
    vertices, edges = get_distance_graph()  # we get distance information.

    # first we find the best order in which we can visit the nodes
    ordered_nodes = __find_order(starting_node, nodes_to_visit, vertices)

    # than the best path to visit them
    best_path = __bellman_ford(ordered_nodes)

    return best_path  # than we return the best path


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


def __bellman_ford(list_to_visit):
    return list_to_visit


""" old functions:
def __find_order_old(start, to_visit, edges):
    ordered_path = [start]  # initialising with the first node, so we can start from the ordered_path[-1] node

    while to_visit:
        found_node = __bfs(ordered_path[-1], to_visit, edges)  # starting from the last node found
        ordered_path.append(found_node)  # append it to the ordered path
        to_visit.remove(found_node)  # removing the node from the searched nodes

    del ordered_path[0]  # deleting the first node, that is start.

    return ordered_path  # returning the ordered path


def __bfs(start, targets, edges):
    # first let's initialise the set that will stores the nodes we visited, we don't want to visit the same node
    # more than once
    visited = set()

    # than creating the queue of the elements to visit
    queue = [start]  # at the beginning we start with our starting node
    visited.add(start)

    while queue:  # iterating until the queue is not empty

        # the lust element in the queue is the one to visit now.
        actual_node = queue.pop()

        if actual_node in targets: return actual_node

        for neighbour, weight in edges[actual_node]:
            if neighbour not in visited:
                queue.insert(0, neighbour)  # at the beginning we start with our starting node
                visited.add(neighbour)

    raise Exception("Node not reachable")  # we didn't find the nodes. them are not reachable than.
"""

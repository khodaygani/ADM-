from utils import get_distance_graph


def functionality(starting_node, nodes_to_visit):
    vertices, edges = get_distance_graph()

    ordered_nodes = __find_order(starting_node, nodes_to_visit, edges)

    best_path = __dijkstra(ordered_nodes)

    return best_path


def __find_order(start, to_visit, edges):
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

    raise Exception("Node not reachable") # we didn't find the nodes. them are not reachable than.


def __dijkstra(list_to_visit):
    return list_to_visit

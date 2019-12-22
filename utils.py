import os
import pickle
from collections import defaultdict


def __prepare_data(path_to_dir=""):  # the paramither is the path where the data is stored.
    # create the folder for the data if is missing
    if not os.path.exists("processed_data\\"):
        os.makedirs("processed_data\\")

    # dict of the nodes and the cordinates
    with open(path_to_dir + 'USA-road-d.CAL.co', 'r') as file:  # get the data
        content = file.read()
    nodes_dict = dict()  # initialize the dict
    for line in content.splitlines():  # foe each line
        if line[0] in ["v"]:  # chek if it's a vertex or an edge
            nodes_dict[int(line.split()[1])] = (int(line.split()[2]), int(line.split()[3]))  # create the dict
    with open('processed_data\\graph.pkl', 'wb') as file:  # saving the dict in a file
        pickle.dump(nodes_dict, file, pickle.HIGHEST_PROTOCOL)

    # process distance data
    with open(path_to_dir + 'USA-road-d.CAL.gr', 'r') as file:  # get the data
        content = file.read()
    dist_dict = __process_data(content)
    with open('processed_data\\distances.pkl', 'wb') as file:  # saving the dict in a file
        pickle.dump(dist_dict, file, pickle.HIGHEST_PROTOCOL)


def __process_data(file_content):
    weight_dict = defaultdict(list)  # initialize the dict
    for measure in file_content.splitlines():  # foe each line
        if measure[0] in ["a"]:  # chek if it's a vertex or an edge
            weight_dict[int(measure.split()[1])].append(
                (int(measure.split()[2]), int(measure.split()[3])))  # create the dict
    return weight_dict  # return the result


def get_time_graph():
    # if the data is not jet parsed we parse it
    if not os.path.exists('processed_data'): __prepare_data()  # saving the data as dictionaries

    with open('processed_data\\graph.pkl', 'rb') as nodes_file:  # get the nodes dict
        nodes_dict = pickle.load(nodes_file)
    # the time dict is to large to save in memory with pickle, so we parse it every time
    with open('USA-road-t.CAL.gr', 'r') as file:  # get the data
        content = file.read()
    time_dict = __process_data(content)
    return nodes_dict, time_dict


def get_distance_graph():
    # if the data is not jet parsed we parse it
    if not os.path.exists('processed_data'): __prepare_data()  # saving the data as dictionaries

    with open('processed_data\\graph.pkl', 'rb') as nodes_file:  # get the nodes dict
        nodes_dict = pickle.load(nodes_file)
    with open('processed_data\\distances.pkl', 'rb') as dist_file:  # get the distances dict
        dist_dict = pickle.load(dist_file)
    return nodes_dict, dist_dict


def find_the_path(distances, start, list_ot_targets):  # for find the best path that pass between al the nodes in order
    path = [start]  # the starting node will be the first node to visit in this path
    for target in list_ot_targets:  # for each node in the target list:
        path += __dijkstra(distances, path.pop(),
                           target)  # we find the best pah for go to that node from the node before

    return path  # finally we return the best path


def __dijkstra(edges, start, target):
    # first let's initialise the set that will stores the nodes we visited, we don't want to visit the same node
    # more than once
    visited_nodes = set()

    # in the dict to each node is saved the shortest path and the cost of that path
    distance_dict = defaultdict(lambda: float("inf"))
    distance_dict[start] = 0  # we add the starting node since we know that is from distance zero from itself
    path_dict = {start: []}  # and the path to reach it is empty

    to_visit_nodes = {start}  # we start with visiting the first node

    # iterating until there are no nodes to visit or we visit the target:
    while to_visit_nodes and target not in visited_nodes:
        # finding the node with the smallest distance from start (from the one not yet visited)
        min_dist = float("inf")
        for node in to_visit_nodes:  # for each node we check witch is the nearest to the starting one
            if distance_dict[node] <= min_dist:
                min_dist = distance_dict[node]
                node_to_visit = node

        # adding each neighbour to the list of nodes to visit, and adding the distance and the path from the start
        for neighbour, weight in edges[node_to_visit]:
            if neighbour not in visited_nodes:  # we do something only if we didn't visit this node yet
                to_visit_nodes.add(neighbour)  # we mark this node as node to visit

                # if the path for reach the neighbour is better than the one saved in the neighbour, we update it
                if distance_dict[neighbour] > distance_dict[node_to_visit] + weight:
                    distance_dict[neighbour] = distance_dict[node_to_visit] + weight
                    path_dict[neighbour] = path_dict[node_to_visit] + [node_to_visit]

        # we have done with this node, we take it out from the to visit nodes and we put it in the visited set.
        to_visit_nodes.discard(node_to_visit)
        visited_nodes.add(node_to_visit)

    if target in visited_nodes:  # if the node is been visited, we return it's best path
        return path_dict[target] + [target]
    else:  # if the node wasn't visited, is not reachable from the the start node.
        raise Exception("Node not reachable")  # we didn't find the node. is not reachable from the starting node than.

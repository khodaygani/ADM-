import os
import pickle
from collections import defaultdict

def prepare_data(path_to_dir=""): #the paramither is the path where the data is stored.
    #create the folder for the data if is missing
    if not os.path.exists("processed_data\\"):
        os.makedirs("processed_data\\")

    #dict of the nodes and the cordinates
    with open(path_to_dir + 'USA-road-d.CAL.co', 'r') as file:  # get the data
        content = file.read()
    nodes_dict = dict()  # initialize the dict
    for line in content.splitlines():  # foe each line
        if line[0] in ["v"]:  # chek if it's a vertex or an edge
            nodes_dict[int(line.split()[1])] = (int(line.split()[2]), int(line.split()[3]))  # create the dict
    with open('processed_data\\graph.pkl', 'wb') as file:  # saving the dict in a file
        pickle.dump(nodes_dict, file, pickle.HIGHEST_PROTOCOL)

    #process distance data
    with open(path_to_dir + 'USA-road-d.CAL.gr', 'r') as file:  # get the data
        content = file.read()
    dist_dict = __process_data(content)
    with open('processed_data\\distances.pkl', 'wb') as file:  # saving the dict in a file
        pickle.dump(dist_dict, file, pickle.HIGHEST_PROTOCOL)

    # process time data
    with open(path_to_dir + 'USA-road-t.CAL.gr', 'r') as file:  # get the data
        content = file.read()
    time_dict = __process_data(content)
    with open('processed_data\\time.pkl', 'wb') as file:  # saving the dict in a file
        pickle.dump(time_dict, file, pickle.HIGHEST_PROTOCOL)

def __process_data(file_content):
    weight_dict = defaultdict(list) #initialize the dict
    for measure in file_content.splitlines(): #foe each line
        if measure[0] in ["a"]: #chek if it's a vertex or an edge
            weight_dict[int(measure.split()[1])].append((int(measure.split()[2]), int(measure.split()[3]))) #create the dict
    return weight_dict #return the result



def get_time_graph():
    with open('processed_data\\graph.pkl', 'rb') as nodes_file:  # get the nodes dict
        nodes_dict = pickle.load(nodes_file)
    with open('processed_data\\time.pkl', 'rb') as time_file:  # get the time dict
        time_dict = pickle.load(time_file)
    return nodes_dict, time_dict


def get_distance_graph():
    with open('processed_data\\graph.pkl', 'rb') as nodes_file:  # get the nodes dict
        nodes_dict = pickle.load(nodes_file)
    with open('processed_data\\time.pkl', 'rb') as dist_file:  # get the distances dict
        dist_dict = pickle.load(dist_file)
    return nodes_dict, dist_dict
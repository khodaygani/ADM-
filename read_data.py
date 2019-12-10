with open('USA-road-d.CAL.co', 'rb') as file:  # saving the dict in a file
    c = file.read()

string = str(c).strip("c 9th DIMACS Implementation Challenge: Shortest Paths\nc http://www.dis.uniroma1.it/~challenge9\nc TIGER/Line nodes coords for graph USA-road-d.CAL\nc\np aux sp co 1890815\nc graph contains 1890815 nodes\nc\nv ")
print(str(c))

with open("test_file.txt", "w") as f:
    f.write(string)
"""
all_elements = c.split(b" -")

dict_of_nodes = {element.split(b" ")[0]: element.split(b" ", 1)[1].split(b" ") for element in all_elements}

print(dict_of_nodes)"""
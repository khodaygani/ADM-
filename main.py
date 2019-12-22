import func_3  # importing functionality 3
import func_4  # importing functionality 4
from plottingUtils import plottingOnMaps  # importing the plotting utils
import sys

if __name__ == '__main__':

    func = int(input("chose your func: ")) #here the user can chose which functionality wants to run


    if func == 1:

        # -------------> insert here your functionality

    elif func == 2:

        # -------------> insert here your functionality

    elif func == 3:
        # getting the input:
        start = int(input("insert the starting node ID: "))

        to_visit = list(map(int, input("insert the targets: ").split(" ")))

        try:  # running the functionality
            nodes, path = func_3.functionality(start, to_visit)
        except Exception:  # if one of those node is not reachable from the start we stop here.
            print("Not possible")
            sys.exit(0)  # stop the program, we don't want to plot.

        plottingOnMaps(nodes, path=path)  # finally plotting!

    elif func == 4:
        # getting the input:
        start = int(input("insert the starting node ID: "))

        to_visit = set(map(int, input("insert the targets: ").split(" ")))

        try:  # running the functionality
            nodes, path = func_4.functionality(start, to_visit)
        except Exception:  # if one of those node is not reachable from the start we stop here.
            print("Not possible")
            sys.exit(0)  # stop the program, we don't want to plot.

        plottingOnMaps(nodes, path=path)  # finally plotting!
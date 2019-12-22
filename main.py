import func_3
import func_4
from plottingUtils import plottingOnMaps
import sys

if __name__ == '__main__':

    func = int(input("chose your func: "))

    if func == 3:

        try:
            nodes, path = func_3.functionality(1, [3, 2, 1766, 1049903])
        except Exception:  # if one of those node is not reachable from the start we stop here.
            print("Not possible")
            sys.exit(0)  # stop the program, we don't want to plot.

        plottingOnMaps(nodes, path=path) #  finally plotting!

    elif func == 4:

        try:
            nodes, path = func_4.functionality(1, {3, 1766, 1049903})
        except Exception: # if one of those node is not reachable from the start we stop here.
            print("Not possible")
            sys.exit(0) #stop the program, we don't want to plot.

        plottingOnMaps(nodes, path=path) #  finally plotting!
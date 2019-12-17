import func_3
import func_4
import sys

if __name__ == '__main__':

    func = int(input("chose your func: "))

    if func == 3:

        try:
            path = func_3.functionality(1, [3, 2, 1766, 1049903])
        except Exception:  # if one of those node is not reachable from the start we stop here.
            print("Not possible")
            sys.exit(0)  # stop the program, we don't want to plot.

        # is the moment to plot

        print("--> The result is: ", path)

    elif func == 4:

        try:
            path = func_4.functionality(1, {3, 1766, 1049903})
        except Exception: # if one of those node is not reachable from the start we stop here.
            print("Not possible")
            sys.exit(0) #stop the program, we don't want to plot.

        # is the moment to plot

        print("--> The result is: ", path)
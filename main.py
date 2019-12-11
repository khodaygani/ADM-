import func_4
import sys

if __name__ == '__main__':

    try:
        path = func_4.functionality(1, set([2,3,4]))
    except Exception:
        print("Not possible")
        sys.exit(0) #stop the program, we don't want to plot.

    print(path)
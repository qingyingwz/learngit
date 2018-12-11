import numpy as np


def loaddata():
    return np.fromfile("ex1data1.txt", int, sep="\n")

if  __name__ == "__mian__":
    traindata = loaddata()
    version = '1.0'
    print(version.startswitch('1'))
    print('end')
    print("Hello the Pycharm!")
import numpy as np

class Logic:

    def swapneeded(self, sortedindex: int, currentarray: np.array):

        if currentarray[sortedindex] < currentarray[sortedindex + 1]:
            return False
        else:
            return True
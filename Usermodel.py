
class Usermodel:
    #gets called by tutot model
    #stores all variables that describe user actions so far

    def __init__(self):
        self.fehler = 0
        self.setMaxTries = 3
        self.tries = 0
        self.endOfList = False
        self.alreadySorted = False


    def resetMaxTries(self):
        self.setMaxTries = 0
    def increaseAttempt(self):
        self.tries += 1
    def setEndOfList(self, truthValue):
        self.endOfList = truthValue
    def setAlreadySorted(self, truthValue):
        self.alreadySorted = truthValue
    def handlestuff(self):
        pass
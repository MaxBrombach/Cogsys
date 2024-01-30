
class Usermodel:
    #calls tutormodel


    def __init__(self):
        self.fehler = 0
        self.maxtries = 3
        self.tries = 0


    def resetMaxtries(self):
        self.maxtries = 0
    def increaseAttempt(self):
        self.tries += 1

    def maxTriesachieved(self):
        if self.maxtries == self.tries:
            return True
        return False

    def handlestuff(self):
        pass
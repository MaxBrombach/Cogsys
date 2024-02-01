
class Usermodel:
    #gets called by tutot model
    #stores all variables that describe user actions so far

    def __init__(self):
        self.fehler = 0
        self.maxtries = 3
        self.tries = 0

    def reset_tries(self):
        self.tries = 0

    def increaseAttempt(self):
        self.tries += 1

    def maxTriesachieved(self):
        if self.maxtries <= self.tries:
            return True
        return False

    def current_tries(self):
        return self.tries

    def handlestuff(self):
        pass
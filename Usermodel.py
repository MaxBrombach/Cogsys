
class Usermodel:
    #calls tutormodel


    def __init__(self):
        self.fehler = 0
        self.setMaxtries = 3
        self.tries = 0


    def resetMaxtries(self):
        self.setMaxtries = 0
    def increaseAttempt(self):
        self.tries += 1

    def handlestuff(self):
        pass
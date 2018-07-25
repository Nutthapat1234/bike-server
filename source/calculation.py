import threading
from time import time as currentTime


class GameCalculationThread(threading.Thread):

    def __init__(self, gameData):
        super().__init__(name="GameCalculationThread")
        self.gameData = gameData
        self.previousTimeStamp = None

    ##############
    ## OVERRIDE ##
    ##############
    def run(self):
        print('start main game calculation thread')
        self.__initialize()
        
        while True:
            deltaTime = self.__calculateDeltaTime()
            self.__updateGame(deltaTime)
            self.__updateTimeStamp()
            print(deltaTime)

    #####################
    ## PRIVATE HELPERS ##
    #####################
    def __initialize(self):
        self.previousTimeStamp = currentTime()
        # TODO: set all values in game data to initial values

    def __calculateDeltaTime(self):
        return currentTime() - self.previousTimeStamp
    
    def __updateGame(self, deltaTime):
        pass
        # TODO: calculate changes

    def __updateTimeStamp(self):
        self.previousTimeStamp = currentTime()
        
        



import threading
from time import time as currentTime

import config


class GameState():
    READY = 0
    PLAY = 1
    END = 2


class GameCalculationThread(threading.Thread):
    
    ############
    ## STATIC ##
    ############
    GAMESTATE = GameState()
    
    def __init__(self, gameData, playerList = {}):
        super().__init__(name="GameCalculationThread")
        self.playerList = playerList
        self.previousTimeStamp = None

    ##############
    ## OVERRIDE ##
    ##############
    def run(self):
        print('start main game calculation thread')
        self.__initialize()
        
        while True:
            self.deltaTime = self.__calculateDeltaTime()
            self.__updateGame(self.deltaTime)
            self.__updateTimeStamp()

    #####################
    ## PRIVATE HELPERS ##
    #####################
    def __initialize(self):
        self.previousTimeStamp = currentTime()
        self.gameState = self.GAMESTATE.READY
        self.playerPositionDict = {}
        self.playerVelocityDict = {}

    def __calculateDeltaTime(self):
        return currentTime() - self.previousTimeStamp
    
    def __updateGame(self, deltaTime):
        if((len(self.playerList)>= 1)and(self.gameState is not self.GAMESTATE.END)):
            self.__setplayerVelocityDict()
            self.__setplayerPositionDict()
            self.__setGameStateByplay()
            #print(self.gameState)

    def __updateTimeStamp(self):
        self.previousTimeStamp = currentTime()

    #####################
    ## PRIVATE SETTER  ##
    #####################
    def __setplayerPositionDict(self):
        for player in self.playerList:
            self.playerPositionDict[player] = player.getPosition()
            
    def __setplayerVelocityDict(self):
        for player in self.playerList:
            self.playerPositionDict[player] = player.getVelocity()
            
    def __setGameStateByplay(self):
        for player,position in self.playerPositionDict.items():
            if(player.getPlayerState() == 2):
                self.gameState = self.GAMESTATE.END
            else:
                self.gameState = self.GAMESTATE.PLAY
                break
            
    ##################
    ## PUBIC SETTER ##
    ##################
    def setGameState(self, gamestate): #Admin
        self.gameState = gamestate

    def setPlayerList(self,playerList):
        self.playerList = playerList

    ##################
    ## PUBIC GETTER ##
    ##################
    def getDeltaTime(self):
        return self.deltaTime
    
    def getPlayerPositionDict(self):
        return self.playerPositionDict
    
    def getGameState(self):
        return self.gameState

   

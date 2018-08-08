import threading
from time import time as currentTime

import config


class GameState():
    READY = 0
    PLAY = 1
    END = 2

class PlayerState():
    STOP = -1
    READY = 0
    RIDE = 1
    FINISH = 2


class GameCalculationThread(threading.Thread):
    
    ############
    ## STATIC ##
    ############
    GAMESTATE = GameState()
    PLAYERSTATE = PlayerState()
    
    def __init__(self, playerList = {}):
        super().__init__(name="GameCalculationThread")
        self.playerList = playerList
        self.previousTimeStamp = None
        self.previousFreq = 0 #use for velocity calculation
        self.allPlayerFinish = 0
        self.gameState = 0

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
        #if((len(self.playerList)>= 1)and(self.gameState is not self.GAMESTATE.END)):
            #self.__setplayerVelocityDict()
            #self.__setplayerPositionDict()
            #self.__setGameStateByplay()

        for player in self.playerList:
            self.__velocityCalculation(player.getGameData())
            self.__positionCalculation(player.getGameData())
            self.__changePlayerState(player.getGameData())
            
            

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
    def getPlayerPositionDict(self):
        return self.playerPositionDict
    
    def getGameState(self):
        return self.gameState
   
    #####################
    ## PRIVATE HELPPER ##
    #####################
    def __positionCalculation(self,player):
        positionchange = player.getVelocity() * self.deltaTime
        if positionchange > config.POSITION_LIMIT:
            pos = player.getPosition()+config.POSITION_LIMIT
            player.setPosition(pos)
        else:
            pos = player.getPosition()+ positionchange
            player.setPosition(pos)

    def __changePlayerState(self,player):
        if (player.getVelocity() < 0):
            player.setPlayerStateByPlay(self.PLAYERSTATE.STOP)
        elif(player.getVelocity() == 0):
            player.setPlayerStateByPlay(self.PLAYERSTATE.READY)
        elif(player.getVelocity() > 0):
            player.setPlayerStateByPlay(self.PLAYERSTATE.RIDE)
        elif(player.getPosition() > 1):
            player.setPlayerStateByPlay(self.PLAYERSTATE.FINISH)
    
    def __velocityCalculation(self,player):
        currentFreq = player.getFrequency()
        if(currentFreq != 0):
            averageFreq = (currentFreq + self.previousFreq)/2
            self.previousFreq =  currentFreq
            velocity = (config.ENDING_POSITION /(config.AVERAGE_TIME*averageFreq))*currentFreq
            player.setVelocity(velocity)

    def __checkGameState(self,player):
        if(player.getPlayerState() == self.PLAYERSTATE.FINISH):
            self.allPlayerFinish += 1

    def __changeGameState(self):
        if(self.allPlayerFinish == 1): #change to config.PLAYER_LIMIT
            self.gameState = self.GAMESTATE.END
        else:
            self.gameState = self.GAMESTATE.PLAY
        
        
        
        1

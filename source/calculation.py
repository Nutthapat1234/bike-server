import threading
from time import time as currentTime

from debugging import print, forcePrint
from config import FREQ_TO_VELOCITY, PLAYER_LIMIT, ENDING_POSITION, BROADCAST_DELAY
from data import GameData, PLAYERSTATE, GAMESTATE

class GameCalculationThread(threading.Thread):
    
    def __init__(self, gameData, connectionList):
        super().__init__(name="GameCalculationThread")
        self.gameData = gameData
        self.connectionList = connectionList
        self.lastSent = currentTime()

    ##############
    ## OVERRIDE ##
    ##############
    def run(self):
        print('start main game calculation thread')
        self.__updateTimeStamp()
        
        while True:
            self.deltaTime = self.__calculateDeltaTime()
            
            self.__updateGame(self.deltaTime)
            self.__updateTimeStamp()
            if currentTime() - self.lastSent >= BROADCAST_DELAY:
                self.__broadcastGameData()
                self.lastSent = currentTime()


    #####################
    ## PRIVATE HELPERS ##
    #####################
    def __broadcastGameData(self):
        
        gameString = str(self.gameData.gameState) + '|'
        
        for playerData in self.gameData.playerDataList:

            if playerData == self.gameData.playerDataList[0]:
                gameString += playerData.getPlayerString()
                #state, pos, velo, x, y, z, w
            else:
                gameString += '|' + playerData.getPlayerString()

        gameString += '\n'
        
        for connection in self.connectionList:
            if not connection.isClient:
                continue
            if connection.exception is not None:
                continue            
            connection.send(gameString)

        print(gameString)
        
    def __calculateDeltaTime(self):
        return currentTime() - self.previousTimeStamp
    
    def __updateGame(self, deltaTime):
        if self.gameData.gameState is GAMESTATE.READY:
            return

        GameCalculator.updateGameState( self.gameData )
        
        if self.gameData.gameState is GAMESTATE.LAUNCHING:
            return
        
        for player in self.gameData.playerDataList:
            GameCalculator.updatePlayerPosition( player, deltaTime )
            GameCalculator.updatePlayerState( player )

        #double check
        GameCalculator.updateGameState( self.gameData )



    def __updateTimeStamp(self):
        self.previousTimeStamp = currentTime()
            
    ###################
    ## PUBIC MUTATOR ##
    ###################
    def resetGame(self):
        self.gameData.reset()

    def startGame(self):
        if self.gameData.gameState is GAMESTATE.READY:
            self.gameData.start()

    ##################
    ## PUBIC GETTER ##
    ##################
    def getPlayerData(self, i):
        return self.gameData.players[i]
    
    def getGameState(self):
        return self.gameData.gameState

   
###########################
## PRIVATE HELPING CLASS ##
###########################
class GameCalculator:
    @staticmethod
    def updatePlayerPosition(player, deltaTime):
        currentFrequency = player.getFrequency()
        currentPosition = player.getPosition()
        
        if currentFrequency is not 0:
##            forcePrint(currentFrequency)
            updatedVelocity = FREQ_TO_VELOCITY * currentFrequency
            updatedPosition = currentPosition + updatedVelocity * deltaTime
            player.setVelocity( updatedVelocity )
            player.setPosition( updatedPosition )
        else:
            player.setVelocity( 0 )
            
    @staticmethod
    def updatePlayerState( player ):
        playerPosition = player.getPosition()
        
        if playerPosition <= 0:
            updatedState = PLAYERSTATE.READY
        elif playerPosition >= ENDING_POSITION:
            updatedState = PLAYERSTATE.FINISHED
        else: # in between (0, 1)
            updatedState = PLAYERSTATE.RIDING

        player.setPlayerState( updatedState )

    @staticmethod
    def updateGameState( gameData ):
        allReady = True
        allFinished = True
        someFinished = False
        
        for player in gameData.playerDataList:
            state = player.getPlayerState()
            if state is not PLAYERSTATE.READY:
                allReady = False
            if state is not PLAYERSTATE.FINISHED:
                allFinished = False
            if state is PLAYERSTATE.FINISHED:
                someFinished = True

        # assuming this method won't be called while gameState is READY
        if allReady and currentTime() - gameData.launchTime < 3:
            updatedState = GAMESTATE.LAUNCHING
        elif allFinished:
            updatedState = GAMESTATE.ALL_FINISHED
        elif someFinished:
            updatedState = GAMESTATE.FIRST_FINISHED
        else:
            updatedState = GAMESTATE.PLAYING_NO_WINNER

        gameData.gameState = updatedState

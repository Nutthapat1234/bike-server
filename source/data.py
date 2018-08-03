import config
from communication import CommunicationThread


class PlayerState():
    STOP = -1
    READY = 0
    RIDE = 1
    FINISH = 2


class GameData():

    ############
    ## STATIC ##
    ############
    PLAYERSTATE = PlayerState()

    def __init__(self,calculationThread = None):
        self.position =  0
        self.zVelocity = 0
        self.frequency = 0
        self.playerState = self.PLAYERSTATE.READY
        self.calculationThread = calculationThread

    ####################
    ## PUBLIC SETTERS ##
    ####################
    def posChange(self,pos):
        self.pos["z"] += pos
        
    def setVelocity(self,freq):
        floatFreq  = float(freq)
        currentFreq = floatFreq
        averageFreq = (currentFreq+self.frequency)/2
        self.frequency = floatFreq
        v = (config.ENDING_POSITION / (config.AVERAGE_TIME*averageFreq))*floatFreq
        self.zVelocity = v
        if(self.position <= config.ENDING_POSITION):
            self.__positionCalculation()
        
    def setPlayerState(self):
        if(self.zVelocity == 0):
            self.playerstate = self.PLAYERSTATE.STOP
        elif(self.zVelocity > 0):
            self.playerstate = self.PLAYERSTATE.RIDE

    ####################
    ## PUBLIC GETTERS ##
    ####################
    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.zVelocity
    
    def getPlayerState(self):
        if (self.zVelocity < 0):
            self.playerstate = self.PLAYERSTATE.STOP
        elif(self.zVelocity == 0):
            self.playerstate = self.PLAYERSTATE.READY
        elif(self.zVelocity > 0):
            self.playerstate = self.PLAYERSTATE.RIDE
        elif(self.position > 1):
            self.playerstate = self.PLAYERSTATE.FINISH
        return self.playerstate

    #####################
    ## PRIVATE HELPPER ##
    #####################
    def __positionCalculation(self):
        if(self.calculationThread is None):
            return
        positionchange = self.zVelocity + self.calculationThread.getDeltaTime()
        if positionchange > config.POSITION_LIMIT:
            self.position += config.POSITION_LIMIT
        else:
            self.position += positionchange
        

        
        

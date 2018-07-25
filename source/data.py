import config

class GameState():
    WAIT = -1
    READY = 0
    PLAY = 1
    END = 2


class PlayerState():
    STUG = -1
    STOP = 0
    RIDE = 1


class GameData():

    ############
    ## STATIC ##
    ############
    GAMESTATE = GameState()
    PLAYERSTATE = PlayerState()

    def __init__(self):
        self.pos =  {"x":0,"y":0,"z":0}
        self.zVelocity = 0
        self.gameState = self.GAMESTATE.WAIT
        self.playerState = self.PLAYERSTATE.STOP

    ####################
    ## PUBLIC SETTERS ##
    ####################
    def posChange(self):
        self.pos["z"] += self.zVelocity #plus avg of loop after
        
    def setVelocity(self,freq):
        v = (config.ENGING_Z_POSITION / config.AVERAGE_TIME) / freq
        self.zVelocity = v

    #sure ?
    #for client(samsung VR) 
    def setGameState(self, gamestate): #Admin
        self.gameState = gamestate

    def setPlayerState(self):
        if(self.zVelocity == 0):
            self.playerstate = self.PLAYERSTATE.STOP
        elif(self.zVelocity > 0):
            self.playerstate = self.PLAYERSTATE.RIDE

    ####################
    ## PUBLIC GETTERS ##
    ####################
    def getGameState(self):
        return self.gameState

    def getPosition(self):
        return self.pos

    def getVelocity(self):
        return self.zVelocity

    

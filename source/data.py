import config


class GameData():

    def __init__(self):
        self.position =  0
        self.zVelocity = 0
        self.frequency = 0
        self.playerState = 0 #Ready

    ####################
    ## PUBLIC SETTERS ##
    ####################
    def setFrequency(self,freq):
        self.frequency =  freq
        
    def setVelocity(self,velocity):
        self.zVelocity = velocity
        
    def setPlayerStateByPlay(self,state):
        self.playerState =  state
            
    def setPosition(self,pos):
        self.position = pos

    ####################
    ## PUBLIC GETTERS ##
    ####################
    def getFrequency(self):
        return self.frequency
        
    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.zVelocity
    
    def getPlayerState(self):
        return self.playerState
    


        

        
        

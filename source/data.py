from config import PLAYER_LIMIT
from debugging import forcePrint
# todo: create getter setter for GameData.

class PLAYERSTATE:
    READY = 0
    RIDING = 1
    FINISHED = 2


class GAMESTATE:
    READY = 0
    PLAYING_NO_WINNER = 1
    FIRST_FINISHED = 2
    ALL_FINISHED = 3


class GameData:
    
    def __init__(self):
         self.reset()

    def reset(self):
        print('game is reset')
        self.gameState = GAMESTATE.READY
        self.playerDataList = [ PlayerData() for i in range(PLAYER_LIMIT) ]
        
    def start( self ):
        print('game is started')
        if self.gameState is GAMESTATE.READY:
            self.gameState = GAMESTATE.PLAYING_NO_WINNER

    def playerOf(self, i):
        return self.playerDataList[i]

    ####################
    ## PUBLIC SETTERS ##
    ####################
    def setFrequency(self, freq, i):
        self.playerOf(i).setFrequency(freq)

    def setVelocity(self, velo, i):
        self.playerOf(i).setVelocity(velo)

    def setPlayerState(self, state, i):
        self.playerOf(i).setPlayerState(state)

    def setPosition(self, position, i):
        self.playerOf(i).setPosition(position)

    def setHeadset(self,w,x,y,z,i):
        self.playerOf(i).setHeadset(w,x,y,z)

    ####################
    ## PUBLIC GETTERS ##
    ####################
    def getFrequency(self, i):
        return self.playerOf(i).getFrequency()

    def getPosition(self, i):
        return self.playerOf(i).getPosition()

    def getVelocity(self, i):
        return self.playerOf(i).getVelocity()

    def getPlayerState(self, i):
        return self.playerOf(i).getPlayerState()

    def getHeadset(self,i):
        return self.playerOf(i).getHeadset()
    
class PlayerData:
    
    def __init__(self):
        self.position =  0
        self.zVelocity = 0
        self.frequency = 0
        self.headset = {}
        self.playerState = PLAYERSTATE.READY

    #################### - we may keep these methods 
    ## PUBLIC SETTERS ## - so that it still looks clean in calculation part
    ####################
    def setFrequency(self,freq):
        self.frequency =  freq
        
    def setVelocity(self,velocity):
        self.zVelocity = velocity
        
    def setPlayerState(self, state):
        self.playerState =  state
            
    def setPosition(self,pos):
        self.position = pos

    def setHeadset(self,w,x,y,z):
        self.headset['w'] = w
        self.headset['x'] = x
        self.headset['y'] = y
        self.headset['z'] = z
        

    ####################
    ## PUBLIC GETTERS ##
    ####################
    def getHeadset(self):
        output = str(self.headset['w'])+','+str(self.headset['x'])+','+str(self.headset['y'])+','+str(self.headset['z'])
        return output
    
    def getFrequency(self):
        return self.frequency
        
    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.zVelocity
    
    def getPlayerState(self):
        return self.playerState
    


        

        
        

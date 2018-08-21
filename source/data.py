from time import time as currentTime

from config import PLAYER_LIMIT
from debugging import forcePrint
# todo: create getter setter for GameData.

class PLAYERSTATE:
    READY = 0
    RIDING = 1
    FINISHED = 2


class GAMESTATE:
    READY = 0
    LAUNCHING = 1
    PLAYING_NO_WINNER = 2
    FIRST_FINISHED = 3
    ALL_FINISHED = 4


class GameData:
    
    def __init__(self):
         self.reset()

    def reset(self):
        print('game is reset')
        self.gameState = GAMESTATE.READY
        self.playerDataList = [ PlayerData() for i in range(PLAYER_LIMIT) ]
        self.launchTime = 0
        
    def start( self ):
        print('game is started')
        if self.gameState is GAMESTATE.READY:
            self.gameState = GAMESTATE.LAUNCHING
        self.launchTime = currentTime()

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

    def getPlayerString(self,i):
        return self.playerOf(i).getPlayerString()

    ####################
    ## short Function ##
    ####################
    def sf(self,freq,i):
        self.setFrequency(freq,i)

    def gf(self,i):
        self.getFrequency(i)

    def sv(self,v,i):
        self.setVelocity(v)
        
    def gv(self,i):
        self.getVelocity(i)

    def sps(self,s,i):
        self.setPlayerState(s,i)

    def gps(self,i):
        self.getPlayerState(i)

    def spo(self,p,i):
        self.setPlayerPosition(p,i)

    def gpo(self,i):
        self.getPlayerPosition(i)

    def sh(self,w,x,y,z,i):
        self.setHeadset(w,x,y,z,i)

    def gh(self,i):
        self.getHeadset(i)

    def gp(self,i):
        self.getPlayerString(i)


class PlayerData:
    
    def __init__(self):
        self.position =  0
        self.zVelocity = 0
        self.frequency = 0
        self.headsetX = 0
        self.headsetY = 0
        self.headsetZ = 0
        self.headsetW = 0
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

    def setHeadset(self,x,y,z,w):
        self.headsetW = w
        self.headsetX = x
        self.headsetY = y
        self.headsetZ = z
        

    ####################
    ## PUBLIC GETTERS ##
    ####################
    def getHeadset(self):
        output = str(self.headsetX)+','+str(self.headsetY)+','+str(self.headsetZ)+','+str(self.headsetW)
        return output
    
    def getFrequency(self):
        return self.frequency
        
    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.zVelocity
    
    def getPlayerState(self):
        return self.playerState

    def getPlayerString(self):
<<<<<<< HEAD
        return str(self.playerState)+','+str(self.position)+','+str(self.zVelocity)+','+str(self.headsetX)+','+str(self.headsetY)+','+str(self.headsetZ)+','+str(self.headsetW)
=======
        return str(self.playerState)+','+format(self.position,'.10f')+','+str(self.zVelocity)+','+str(self.headsetX)+','+str(self.headsetY)+','+str(self.headsetZ)+','+str(self.headsetW)


        

        
        
>>>>>>> master

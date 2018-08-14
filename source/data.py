from config import PLAYER_LIMIT

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
         self.players = {}
         self.index = 0
         self.reset()

    def reset(self):
        print('game is reset')
        self.gameState = GAMESTATE.READY
        self.playerDataList = [ PlayerData() for i in range(PLAYER_LIMIT) ]
        if len(self.players) != 0:
            index = 0
            for player in players:
                self.players[player] = self.playerDataList[index]
                index += 1
        

    def start( self ):
        print('game is started')
        if self.gameState is GAMESTATE.READY:
            self.gameState = GAMESTATE.PLAYING_NO_WINNER

    def setPlayerTag(self,tag):
        self.players[tag] = self.playerDataList[self.index]
        self.index += 1

        
class PlayerData:
    
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
        
    def setPlayerState(self, state):
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
    


        

        
        

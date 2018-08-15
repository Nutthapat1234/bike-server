import socket
import threading

from debugging import print
from config import PORT

class CommunicationThread(threading.Thread):

    def __init__(self, connection, addr, shareGameData):
        super().__init__(name="CommunicationThread to " + str(addr))
        
        self.connection = connection
        self.address = addr
        self.shareGameData = shareGameData
        self.__isRunning = True
        self.exception =  None
        self.isClient = False
        
    ##############
    ## OVERRIDE ##
    ##############
    def run(self):
        print('start handling gameClientConnection', self.address)

        try:
            while self.__isRunning:
                data = self.connection.recv(1024)
                data = data.decode('utf-8')
                buffer = data.split('\n')
                buffer = buffer[:-1]

                while len(buffer) > 0:
                    command = buffer.pop(0)
                    print('execute command:', command, ': from', self.address[0])
                    self.respondClient(command)
##                    threading.Thread(target=self.respondClient,args=[command]).start()
    
        except socket.error as msg:
            while self.__isRunning:  
                self.connection.close()
                self.exception = ConnectionResetError()
            
                          
    def respondClient(self,data):
        try:
            result = self.__executeCommand(data)
            
            if result is not None:
                self.connection.send(str.encode(str(result)))
        except socket.error :
                self.exception = ConnectionResetError()
                return

    ############
    ## PUBLIC ##
    ############
    def getConnection(self):
        return self.connection

    def getAddress(self):
        return self.address
    
    def getException(self):
        return self.exception
    
    def exit(self):
        self.__isRunning = False
        
    def tagClient(self):
        if self.isClient:
            return
        #may create another sending thread
        self.isClient = True
    
    #####################
    ## PRIVATE HELPERS ##
    #####################
    def __executeCommand(self, strDataIn):
        try: #to call method according to header
            dataIn =    self.__convertToTuple(strDataIn) #convert to tuple
            header =    self.__extractHeader(dataIn)
##            tag    =    self.__extractTag(dataIn)
            values =    self.__extractParameters(dataIn)

            actionMethod = self.__getCorrespondingMethod(header)
            output = self.__performAction(actionMethod, values)
            
            return output
            
        except Exception as e:
            print('error found for request:', strDataIn)
            print('with exception:', e.format_exc())
            
            return None

    def __convertToTuple(self, strData):
        # <--example--> convert "'getGameState'," to ('gameState',)
        manipulatedString = '('+strData+')'
        return eval(manipulatedString)
    
##    def __extractTag(self, tupleData):
##        return tupleData[0]
    
    def __extractHeader(self, tupleData):
        return tupleData[0]
    
    def __extractParameters(self, tupleData):
        return tupleData[1:]

    def __getCorrespondingMethod(self, header):
        #admin actions
        if header == 'tagClient':
            return self.tagClient
        
        if header == 'reset':
            return self.shareGameData.reset

        if header == 'start':
            return self.shareGameData.start

        if header == 'setPlayerTag':
            return self.shareGameData.setPlayerTag
        
        #client actions
        return getattr(self.shareGameData, header)

    def __performAction(self, actionMethod, values):
        return actionMethod(*values)
        



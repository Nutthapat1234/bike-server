import socket
import threading


class CommunicationThread(threading.Thread):

    def __init__(self, connection, addr, gameData):
        super().__init__(name="CommunicationThread to " + str(addr))
        
        self.connection = connection
        self.address = addr
        self.gameData = gameData

    ##############
    ## OVERRIDE ##
    ##############
    def run(self):
        print('start handling gameClientConnection', self.address)
        
        while True:
            data = self.connection.recv(1024)
            data = data.decode('utf-8')
            print('received data from', self.address, ':', data)
            result = self.__executeCommand(data)
            print('get result:', result)

    ############
    ## PUBLIC ##
    ############
    def getConnection(self):
        return self.connection

    def getAddress(self):
        return self.address

    #####################
    ## PRIVATE HELPERS ##
    #####################
    def __executeCommand(self, strDataIn):
        try: #to call method according to header
            dataIn =    self.__convertToTuple(strDataIn) #convert to tuple
            header =    self.__extractHeader(dataIn)
            values =    self.__extractParameters(dataIn)

            actionMethod = self.__getCorrespondingMethod(header)
            output = self.__performAction(actionMethod, values)
            
            return output
            
        except Exception as e:
            print('error found for request:', strDataIn)
            print('with exception:', e)
            
            return None

    def __convertToTuple(self, strData):
        # <--example--> convert "'getGameState'," to ('gameState',)
        manipulatedString = '('+strData+')'
        return eval(manipulatedString)
    
    def __extractHeader(self, tupleData):
        return tupleData[0]
    
    def __extractParameters(self, tupleData):
        return tupleData[1:]

    def __getCorrespondingMethod(self, header):
        return getattr(self.gameData, header)

    def __performAction(self, actionMethod, values):
        return actionMethod(*values)
        



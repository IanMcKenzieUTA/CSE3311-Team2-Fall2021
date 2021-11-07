from werkzeug.security import check_password_hash,generate_password_hash
from UserLogin.TurkInfo import TurkInfo
from UserLogin.ResultUser import ResultUser
from ast import literal_eval
from helpers import UploadS3, DynamoDBTurk
import os
#from helpers import  DynamoDB
import binascii
class TurkLoader:
    def __init__(self):
        self.turkUserList = self.getTurkUserList()    
        
    def getCurrentUser(self,turkToken):
#        self.userList = self.getUserList()
        if turkToken in self.turkUserList:
            return TurkInfo(turkToken,self.turkUserList[turkToken]['drawings'],int(self.turkUserList[turkToken]['drawingCount']),int(self.turkUserList[turkToken]['successCount']),self.turkUserList[turkToken]['successDrawing'],self.turkUserList[turkToken]['Approved'])
        else:
            self.turkUserList = self.getTurkUserList()
            if turkToken in self.getTurkUserList:
                return TurkInfo(turkToken,self.turkUserList[turkToken]['drawings'],int(self.turkUserList[turkToken]['drawingCount']),int(self.turkUserList[turkToken]['successCount']),self.turkUserList[turkToken]['successDrawing'],self.turkUserList[turkToken]['Approved'])
            else: 
                return TurkInfo(turkToken)
            
    def setNewUser(self):
        turkToken= self.generateToken()
        while turkToken in self.turkUserList:
            turkToken=  self.generateToken()
        turkUser = TurkInfo(turkToken)
        DynamoDBTurk.creteNewItem(turkUser)
        return turkToken

    def generateToken(self):
        byteToken = os.urandom(12)
        hexToken = binascii.hexlify(byteToken)
        return hexToken.decode("utf-8")

    def setNewDrawing(self,turkUser,drawinName):
        turkUser.setNewDrawing(drawinName) 
        self.turkUserList[turkUser.turkToken] = turkUser.getUserInfo()
#        hey =curUser.getUserInfo() 
#        print(hey['drawingCount'])
        DynamoDBTurk.updateItem(turkUser.turkToken, 'drawings',turkUser.drawings )
        DynamoDBTurk.updateItem(turkUser.turkToken, 'drawingCount',turkUser.drawingsCount )
        return turkUser  
    
  
    
    def setNewDrawings(self,turkUser,drawings):
        for drawing in drawings:
             self.setNewDrawing(turkUser,drawing)
        


    def getTurkUserList(self):
        usertList= DynamoDBTurk.getUserList()
        return usertList
    
    

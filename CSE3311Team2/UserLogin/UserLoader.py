from werkzeug.security import check_password_hash,generate_password_hash
from UserLogin.UserInfo import UserInfo
from UserLogin.ResultUser import ResultUser
from ast import literal_eval
from helpers import UploadS3, DynamoDB
import operator
#from helpers import  DynamoDB

class UserLoader:
            
    def __init__(self):
        self.userList = self.getUserList()         
    
    def getCurrentUser(self,userID):
#        self.userList = self.getUserList()
        if userID in self.userList:
            return UserInfo(userID,self.userList[userID]['emailID'], self.userList[userID]['passWord'], self.userList[userID]['turkID'],self.userList[userID]['drawings'],int(self.userList[userID]['drawingCount']),int(self.userList[userID]['successCount']),self.userList[userID]['successDrawing'],self.userList[userID]['consent'] )
        else:
            self.userList = self.getUserList()
            if userID in self.userList:
                return UserInfo(userID,self.userList[userID]['emailID'], self.userList[userID]['passWord'], self.userList[userID]['turkID'],self.userList[userID]['drawings'],int(self.userList[userID]['drawingCount']),int(self.userList[userID]['successCount']),self.userList[userID]['successDrawing'],self.userList[userID]['consent'] )
            else: 
                return UserInfo()
            
    def checkUserPassword(self, userID, password):
        if userID in self.userList:
            result = check_password_hash(self.userList[userID]['passWord'], password)
            if result:
                registerUSer = ResultUser("Log In Successful", True)
                return registerUSer
            else:
                registerUSer = ResultUser("Password doesn't match", False)
                return registerUSer  
                
        else:
            self.userList = self.getUserList()
            if userID in self.userList:
                result = check_password_hash(self.userList[userID]['passWord'], password)
                if result:
                    registerUSer = ResultUser("Log In Successful", True)
                    return registerUSer
                else:
                    registerUSer = ResultUser("Password doesn't match", False)
                return registerUSer  
            else:
                registerUSer = ResultUser("User ID Not found", False)
        return registerUSer


    def printUSerList(self):
        for item in self.userList:
            print(self.userList[item])
            
            
    def setNewUser(self,curUser):
#        self.userList = self.getUserList()          

        if self.checkEmailAvailability(curUser.emailID):
            registerUSer = ResultUser("E-mail ID exists", False)
            return registerUSer
        if curUser.userID in self.userList:
            registerUSer = ResultUser("User ID exists", False)
            return  registerUSer
        curUser.passWord = generate_password_hash(curUser.passWord)
#        self.userList [curUser.userID] = curUser.getUserInfo()
#        self.printUSerList()
#        UploadS3.writeUserInfo(str(self.userList))
#        text_file  = open(self.userPath, 'w+')
#        text_file.write(str(self.userList))
#        text_file.close()
        DynamoDB.creteNewItem(curUser)
        registerUSer = ResultUser("Registered Successfully", True)
        return registerUSer

#    def changeCurUser(self,curUser ):
#        self.userList = self.getUserList()
#        self.userList [curUser.userID] = curUser.getUserInfo()
#        UploadS3.writeUserInfo(str(self.userList))

    def setNewDrawing(self,curUser,drawinName):
        curUser.setNewDrawing(drawinName) 
        self.userList[curUser.userID] = curUser.getUserInfo()
#        hey =curUser.getUserInfo() 
#        print(hey['drawingCount'])
        DynamoDB.updateItem(curUser.userID, 'drawings',curUser.drawings )
        DynamoDB.updateItem(curUser.userID, 'drawingCount',curUser.drawingsCount )
        return curUser  
    
    def setConsent(self,curUser):
        DynamoDB.updateItem(curUser.userID, 'consent',1 )
        return   
    
    def setNewDrawings(self,curUser,drawings):
        for drawing in drawings:
             self.setNewDrawing(curUser,drawing)
#        drawingNames = [x for x in drawings]
#        curUser.setNewDrawings(drawingNames) 
#        self.changeCurUser(curUser)
#        return curUser
        
    def setNewPassword(self,curUser,password):
        curUser.passWord = generate_password_hash(password)
        self.userList[curUser.userID] = curUser.getUserInfo()
        DynamoDB.updateItem(curUser.userID, 'passWord',curUser.passWord )
#        self.changeCurUser(curUser)
        
        
    def checkEmailAvailability(self, email):
        self.userList = self.getUserList()
        for user in self.userList:
            userInfo = self.userList[user]
            if userInfo['emailID'] == email:
                return True
        return False

    def getUserIDFromEmail(self, email):
        userID = ""
        for user in self.userList:
            userInfo = self.userList[user]
            if userInfo['emailID'] == email:
                 userID = user
        return userID


    def getUserList(self):
        usertList= DynamoDB.getUserList()
#        usertList = {}
#        try:
#            usertList = literal_eval(fileContent)
#        except:
#              print(usertList)  
        
#        print(usertList)
        return usertList
    
    
    def getLeaderBoard(self, curUser):
        if curUser.userID == 'Guest':
            modifiedUserList = dict(self.userList)
            modifiedUserList.pop('Guest')
            resultList = []
            counts = {x: [modifiedUserList[x]['drawingCount'],modifiedUserList[x]['successCount']] for x in modifiedUserList}
            sorted_x = sorted(counts.items(), key=operator.itemgetter(1),reverse=True)
            resultList = sorted_x[0:4]
            resultList.append([1,2,3,4])
            return resultList
        
        modifiedUserList = dict(self.userList)
        modifiedUserList.pop('Guest')
        resultList = []
        counts = {x: [modifiedUserList[x]['drawingCount'],modifiedUserList[x]['successCount']] for x in modifiedUserList}
#        sorted_x = sorted(counts.items(), key=operator.itemgetter(1),reverse=True)
        sorted_x = sorted(counts.items(),key=lambda elem: elem[1][0],reverse=True)
        index = sorted_x.index((curUser.userID,[curUser.drawingsCount,curUser.successCount]))
        print(index)
        if index<3:
            resultList = sorted_x[0:4]
            resultList.append([1,2,3,4])
        elif index== len(sorted_x)-1:
            resultList.append(sorted_x[0])
            resultList.append(sorted_x[index-2])
            resultList.append(sorted_x[index-1])
            resultList.append(sorted_x[index])
            resultList.append([1,index-1,index,index+1])
        else:
            resultList.append(sorted_x[0])
            resultList.append(sorted_x[index-1])
            resultList.append(sorted_x[index])
            resultList.append(sorted_x[index+1])
            resultList.append([1,index,index+1,index+2])

        return  resultList

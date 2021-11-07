class UserInfo:            
    def __init__(self, userID="Guest", emailID="Guest", passWord="Guest", turkID="Guest", drawings=[],drawingsCount=0, successCount=0,successDrawing=[], consent= False ):
        self.userID = userID
        self.emailID = emailID
        self.passWord = passWord
        self.turkID = turkID
        self.drawings = drawings
        self.drawingsCount = drawingsCount
        self.successCount = successCount
        self.consent = consent
        self.successDrawing = successDrawing
        
    def getUserInfo(self):
        userInfo = {'emailID':self.emailID, 'passWord':self.passWord, 'turkID': self.turkID,'drawingCount': self.drawingsCount, 'drawings':self.drawings, 'successCount': self.successCount,'successDrawing': self.successDrawing,'consent': self.consent }
        return userInfo
    
    def setNewDrawings(self, newDrawings):
        self.drawings.extend(newDrawings)
        self.drawingsCount =    self.drawingsCount + len(newDrawings)
        
    def setNewDrawing(self, newDrawing):
        self.drawings.append(newDrawing)
        self.drawingsCount =   self.drawingsCount +1
class TurkInfo:            
    def __init__(self, turkToken, drawings=[],drawingsCount=0, successCount=0,successDrawing=[], approval=0):
        self.turkToken = turkToken
        self.drawings = drawings
        self.drawingsCount = drawingsCount
        self.successCount = successCount
        self.successDrawing = successDrawing
        self.approve = approval
        
    def getUserInfo(self):
        userInfo = {'drawingCount': self.drawingsCount, 'drawings':self.drawings, 'successCount': self.successCount,'successDrawing': self.successDrawing,'Approved': self.approve }
        return userInfo
    
    def setNewDrawings(self, newDrawings):
        self.drawings.extend(newDrawings)
        self.drawingsCount =    self.drawingsCount + len(newDrawings)
        
    def setNewDrawing(self, newDrawing):
        self.drawings.append(newDrawing)
        self.drawingsCount =   self.drawingsCount +1
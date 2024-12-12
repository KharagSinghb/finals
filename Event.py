class Event:
    def __init__(self, eventID,eventLocation,category):
        self.eventID = eventID
        self.eventLocation = eventLocation
        self.category = category

    def getEventId(self):
        return self.EventId 
         
    def seteventLocation(self,new_eventLocation):
        self.eventLocation = new_eventLocation
        if len(new_eventLocation) :
            raise Exception("The string is empty")
        
        for char in new_eventLocation:
            if char.isdigit():
                raise ValueError("there are numbers in the string")
            
    def calculateEventFee(self,fee,tax,total):
        self.tax = 0.135
        self.total = self.fee * self.tax









import Event
class SpecialEvent(Event):
    def __init__(self,eventID,eventLocation,category,special_event_category):
        super().__init__(eventID,eventLocation,category)
        self.special_event_category = special_event_category
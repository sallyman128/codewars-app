class Event:
    def __init__(self, eventType, payload):
        self.eventType = eventType
        self.payload = payload

    def to_dict():
        return {
            eventType: self.eventType,
            payload: self.payload
        }
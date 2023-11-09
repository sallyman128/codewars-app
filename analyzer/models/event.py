class Event:
    def __init__(self, message, payload):
        self.message = message
        self.payload = payload

    def to_dict():
        return {
            message: self.message,
            payload: self.payload
        }
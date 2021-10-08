class Logger:

    def __init__(self):
        
        self._msg_dict = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if self._msg_dict.get(message) is None:
            self._msg_dict[message] = timestamp
            return True
        elif timestamp - self._msg_dict[message] >= 10:
            self._msg_dict[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

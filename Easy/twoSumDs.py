class TwoSum:

    def __init__(self):
        self.numsDict = {}
        
    def add(self, number: int) -> None:
        if self.numsDict.get(number):
            self.numsDict[number] += 1
        else:
            self.numsDict[number] = 1
        

    def find(self, value: int) -> bool:
        
        for num in self.numsDict.keys():
            secondElem = value - num
            
            if num == secondElem and self.numsDict[secondElem] == 1:
                continue
            
            if self.numsDict.get(secondElem):
                return True

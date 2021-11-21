#time O(n)
#space O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        lenTemperatures = len(temperatures)
        answer = [0]*lenTemperatures
        stack = []
        
        for currDay, currTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currTemp:
                prevDay = stack.pop()
                answer[prevDay] = currDay - prevDay
            stack.append(currDay)
        return answer

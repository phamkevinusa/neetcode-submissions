class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempstack = [] # [index, temp]
        result = len(temperatures) * [0]
        for i, temp in enumerate(temperatures):
            while tempstack and temp > tempstack[-1][1]:
                stackInd, StackT = tempstack.pop()
                result[stackInd] = i - stackInd
            tempstack.append([i, temp])

        return result
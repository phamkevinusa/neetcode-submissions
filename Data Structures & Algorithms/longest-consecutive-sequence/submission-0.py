class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = []
        length = 0
        if not nums:
            return 0
        for num in nums:
            if num - 1 not in numSet:
                temp = []
                while num in numSet:
                    temp.append(num)
                    if len(temp) > length:
                        length = len(temp)
                        res = temp
                    num = num + 1
        return length
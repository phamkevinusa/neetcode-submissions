class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        choices = []

        def dfs(choices):
            if not choices:
                res.append(cur.copy())
                return
            for i, num in enumerate(choices):
                temp = choices.copy()
                cur.append(num)
                temp.pop(i)
                dfs(temp)

                cur.pop()

        dfs(nums)
        return res
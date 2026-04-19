class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        temp = 0
        while tokens:
            print(nums)
            token = tokens.pop(0)
            

            if token == "+":
                nums.append(nums.pop() + nums.pop())
                continue
            if token == "-":
                i = nums.pop()
                j = nums.pop()
                nums.append(j-i)
                continue
            if token == "*":
                nums.append(nums.pop() * nums.pop())
                continue
            if token == "/":
                i = nums.pop()
                j = nums.pop()
                nums.append(int(j / i))
                continue

            else:
                nums.append(int(token))

        return nums.pop()
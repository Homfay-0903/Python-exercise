class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        subfix = [0] * n
        res = [0] * n

        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        subfix[-1] = 1
        for i in range(n - 2, -1, -1):
            subfix[i] = subfix[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix[i] * subfix[i]

        return res
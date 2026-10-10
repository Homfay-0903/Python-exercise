class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        cur_num = nums[0]
        max_num = nums[0]

        for i in range(1, n):
            cur_num = max(nums[i], cur_num + nums[i])
            max_num = max(max_num, cur_num)

        return max_num

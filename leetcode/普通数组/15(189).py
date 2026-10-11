class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k:
            return

        n = len(nums)
        k = k % n

        front_nums = nums[:n - k]
        back_nums = nums[n - k:]
        nums[:] = back_nums + front_nums
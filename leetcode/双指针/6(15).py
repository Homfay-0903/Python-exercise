class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            first_idx = i
            left, right = i + 1, n - 1

            while left < right:
                cur_sum = nums[first_idx] + nums[left] + nums[right]

                if cur_sum == 0:
                    res.append([nums[first_idx], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1

        return res
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[num] = i
            
        return []
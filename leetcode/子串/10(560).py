class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        total = 0
        res = 0

        for num in nums:
            total += num

            if (total - k) in prefix_count:
                res += prefix_count[total - k]

            prefix_count[total] = prefix_count.get(total, 0) + 1

        return res
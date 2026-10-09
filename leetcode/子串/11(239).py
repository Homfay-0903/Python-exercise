from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        res = []

        for i in range(n):
            while queue and queue[0] < i + 1 - k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if i + 1 - k >= 0:
                res.append(nums[queue[0]])

        return res
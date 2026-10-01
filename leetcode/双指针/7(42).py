class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0
        left, right = 0, n - 1
        leftHighest, rightHighest = 0, 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > leftHighest:
                    leftHighest = height[left]
                else:
                    res += leftHighest - height[left]
                left += 1
            else:
                if height[right] > rightHighest:
                    rightHighest = height[right]
                else:
                    res += rightHighest - height[right]
                right -= 1

        return res
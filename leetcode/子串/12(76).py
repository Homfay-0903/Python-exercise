from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        valid = 0
        left = 0
        start, length = 0, float('inf')

        for right, char in enumerate(s):
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid += 1

                while valid == len(need):
                    if right - left + 1 < length:
                        start, length = left, right - left + 1

                    removeChar = s[left]
                    left += 1

                    if removeChar in need:
                        if window[removeChar] == need[removeChar]:
                            valid -= 1
                        window[removeChar] -= 1

        return "" if length == float('inf') else s[start:start + length]
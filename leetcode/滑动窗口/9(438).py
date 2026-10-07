class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        res = []

        if s_len < p_len:
            return res

        count_p = [0] * 26
        count_window = [0] * 26

        base = ord('a')

        for i in range(p_len):
            p_char_idx = ord(p[i]) - base
            s_char_idx = ord(s[i]) - base
            count_p[p_char_idx] += 1
            count_window[s_char_idx] += 1

        if count_p == count_window:
            res.append(0)

        for i in range(p_len, s_len):
            cur_char_idx = ord(s[i]) - base
            pre_char_idx = ord(s[i - p_len]) - base

            count_window[pre_char_idx] -= 1
            count_window[cur_char_idx] += 1

            if count_p == count_window:
                res.append(i - p_len + 1)

        return res
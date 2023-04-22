# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left, length = 0, len(s)
        cur_len, max_len = 0, 0
        lookup = set()
        for i in range(length):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            lookup.add(s[i])
            max_len = cur_len if cur_len > max_len else max_len
        return max_len


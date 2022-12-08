# Given a string s, find the length of the longest substring without repeating characters.

'''
>>> s = Solution()
>>> s.lengthOfLongestSubstring('abcabcbb')
3
>>> s = Solution()
>>> s.lengthOfLongestSubstring('bbbbb')
1
>>> s = Solution()
>>> s.lengthOfLongestSubstring('pwwkew')
3
>>> s = Solution()
>>> s.lengthOfLongestSubstring('sjvjh')
3
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # last occurance dic
        dic = {}
        str_now, max = '', 0
        for i in range(len(s)):
            if s[i] not in str_now:
                str_now += s[i]
            else:
                if len(str_now) > max:
                    max = len(str_now)
                str_now = s[(dic.setdefault(s[i]) + 1) : i] + s[i]
            dic[s[i]] = i
        if len(str_now) > max:
            max = len(str_now)
        return max

if __name__ == '__main__':
    import doctest
    doctest.testmod()
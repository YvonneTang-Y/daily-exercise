# Given a string s, return the longest palindromic substring in s.

'''
>>> s = Solution()
>>> s.longestPalindrome("babad")
'bab'
>>> s = Solution()
>>> s.longestPalindrome("cbbd")
'bb'
>>> s = Solution()
>>> s.longestPalindrome("cbbc")
'cbbc'
>>> s = Solution()
>>> s.longestPalindrome("bbb")
'bbb'

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = s[0]
        str = s[0]
        # let s[i] be the center of Palindromic Substring
        for i in range(len(s)):
            count = 1
            # check the length of center
            while i + count < len(s) and s[i] == s[i + count]:
                count += 1
            
            m, n = i - 1, i + count
            # verify from center to both ends
            while m >= 0 and n <= len(s) - 1:
                if s[m] != s[n]:
                    str = s[m + 1 : n]
                    if len(str) > len(max_str):
                        max_str = str
                    break
                m -= 1
                n += 1
            str = s[m + 1 : n]
            if len(str) > len(max_str):
                max_str = str            

        return max_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
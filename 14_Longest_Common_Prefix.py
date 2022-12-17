# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

'''
>>> s = Solution()
>>> s.longestCommonPrefix(["flower","flow","flight"])
'fl'
>>> s = Solution()
>>> s.longestCommonPrefix(["dog","racecar","car"])
''

'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        pattern = min(strs, key = len)
        s = ''
        for i in range(len(pattern)):
            for j in strs:
                if j[i] != pattern[i]:
                    return s

            s += pattern[i]
        return s
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
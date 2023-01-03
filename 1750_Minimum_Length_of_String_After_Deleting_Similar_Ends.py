# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).


'''
>>> s = Solution()
>>> s.minimumLength('ca')
2
>>> s = Solution()
>>> s.minimumLength('cabaabac')
0
>>> s = Solution()
>>> s.minimumLength('aabccabba')
3
>>> s = Solution()
>>> s.minimumLength('bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb')
1

'''


class Solution:
    def minimumLength(self, s: str) -> int:
        lindex = 0
        rindex = len(s) - 1
        while lindex < rindex and s[lindex] == s[rindex]:
            tmp = s[lindex]
            while lindex <= len(s) - 1 and s[lindex] == tmp:
                lindex += 1
            while rindex >= 0 and s[rindex] == tmp:
                rindex -= 1
        return max(rindex - lindex + 1, 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
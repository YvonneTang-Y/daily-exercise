# Given an integer x, return true if x is a palindrome, and false otherwise.

'''
>>> s = Solution()
>>> s.isPalindrome(121)
True
>>> s = Solution()
>>> s.isPalindrome(-121)
False
>>> s = Solution()
>>> s.isPalindrome(10)
False

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
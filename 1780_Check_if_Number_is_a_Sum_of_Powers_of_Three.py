# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3^x.


'''
>>> s = Solution()
>>> s.checkPowersOfThree(12)
True
>>> s = Solution()
>>> s.checkPowersOfThree(91)
True
>>> s = Solution()
>>> s.checkPowersOfThree(21)
False

'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 > 1:
                return False
            n = n // 3
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

'''
>>> s = Solution()
>>> s.reverse(123)
321
>>> s = Solution()
>>> s.reverse(-123)
-321
>>> s = Solution()
>>> s.reverse(120)
21

'''

from math import pow
class Solution:
    def reverse(self, x: int) -> int:
        s = ''
        if x < 0:
            s = '-'
        lis = list(str(abs(x)))
        lis.reverse()
        s += ''.join(lis)

        num = int(s)
        if num >= pow(-2, 31) and num < pow(2, 31):
            return num
    
        return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
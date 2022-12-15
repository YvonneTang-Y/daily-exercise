# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

'''
>>> s = Solution()
>>> s.intToRoman(3)
'III'
>>> s = Solution()
>>> s.intToRoman(58)
'LVIII'
>>> s = Solution()
>>> s.intToRoman(1994)
'MCMXCIV'

'''

class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        s = ''
        for key, value in dic.items():
            while num >= key:
                num -= key
                s += value
        return s

if __name__ == '__main__':
    import doctest
    doctest.testmod()
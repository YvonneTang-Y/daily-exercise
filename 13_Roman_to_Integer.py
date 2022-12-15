# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

'''
>>> s = Solution()
>>> s.romanToInt('III')
3
>>> s = Solution()
>>> s.romanToInt('LVIII')
58
>>> s = Solution()
>>> s.romanToInt('MCMXCIV')
1994

'''

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        i = len(s) - 1
        num = 0
        while i >= 0:
            if i > 0 and dic[s[i]] > dic[s[i - 1]]:
                num += dic[s[i]] - dic[s[i - 1]]
                i -= 2
            else:
                num += dic[s[i]]
                i -= 1
        return num

if __name__ == '__main__':
    import doctest
    doctest.testmod()
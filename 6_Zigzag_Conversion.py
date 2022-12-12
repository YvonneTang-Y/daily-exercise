# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

'''
>>> s = Solution()
>>> s.convert("PAYPALISHIRING", 3)
'PAHNAPLSIIGYIR'
>>> s = Solution()
>>> s.convert("PAYPALISHIRING", 4)
'PINALSIGYAHRPI'
>>> s = Solution()
>>> s.convert("A", 1)
'A'

'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        count = 0
        list = [[] for _ in range(numRows)]
        for e in s:
            if count % (2 * numRows - 2) < numRows:
                list[count % (2 * numRows - 2)].append(e)
            else:
                for i in range(numRows):
                    list[i].append('')
                list[numRows - count % (2 * numRows - 2) - 2][-1] = e
            count += 1
        str = ''
        for i in list:
            str += ''.join(i)
        return str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
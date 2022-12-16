# You are given a string s consisting of lowercase English letters, and an integer k.

# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.

'''
>>> s = Solution()
>>> s.getLucky('iiii',1)
36
>>> s = Solution()
>>> s.getLucky('leetcode',2)
6
>>> s = Solution()
>>> s.getLucky('zbax',2)
8
'''



class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''.join(str(ord(i) - 96) for i in s)
        while k > 0:
            if len(num) == 1:
                break
            count = sum((int(e)) for e in num)
            num = str(count)
            k -= 1
        return int(num)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

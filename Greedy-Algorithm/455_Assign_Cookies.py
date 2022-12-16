# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

'''
>>> s = Solution()
>>> s.findContentChildren([1,2,3], [1,1])
[7,0,8]
>>> s = Solution()
>>> s.findContentChildren([1,2], [1,2,3])
[0]

'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index = 0
        for i in s:
            # check each cookie to ensure that the next child can be satisfied
            if index < len(g) and g[index] <= i:
                index += 1
        return index

if __name__ == '__main__':
    import doctest
    doctest.testmod()
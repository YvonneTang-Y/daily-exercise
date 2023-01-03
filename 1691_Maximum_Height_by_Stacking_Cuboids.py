# Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

# You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

# Return the maximum height of the stacked cuboids.

'''
>>> s = Solution()
>>> s.maxHeight([[50,45,20],[95,37,53],[45,23,12]])
190
>>> s = Solution()
>>> s.maxHeight([[38,25,45],[76,35,3]])
76
>>> s = Solution()
>>> s.maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]])
102
'''

class Solution:
    def maxHeight(self, cuboids) -> int:
        # sort list
        for i in cuboids:
            i.sort(reverse = True)
        cuboids.sort(key=sum, reverse = True)

        # dynamic programming
        dp = [0] * len(cuboids)
        for i in range(len(cuboids)):
            dp[i] = cuboids[i][0]
            for j in range(i):
                if cuboids[j][0] >= cuboids[i][0] and cuboids[j][1] >= cuboids[i][1] and cuboids[j][2] >= cuboids[i][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][0])

        return max(dp)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
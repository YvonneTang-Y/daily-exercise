# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

'''
>>> s = Solution()
>>> s.maxArea([1,1])
1
>>> s = Solution()
>>> s.maxArea([1,8,6,2,5,4,8,3,7])
49

'''

class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        maxA = 0
        while left < right:
            maxA = max(maxA, (right - left) * min(height[left], height[right]))
            if height[left] >= height[right]:
                right -=1
            else:
                left += 1
        return maxA

if __name__ == '__main__':
    import doctest
    doctest.testmod()
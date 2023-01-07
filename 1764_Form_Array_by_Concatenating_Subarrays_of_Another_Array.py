# You are given a 2D integer array groups of length n. You are also given an integer array nums.

# You are asked if you can choose n disjoint subarrays from the array nums such that the ith subarray is equal to groups[i] (0-indexed), and if i > 0, the (i-1)th subarray appears before the ith subarray in nums (i.e. the subarrays must be in the same order as groups).

# Return true if you can do this task, and false otherwise.

# Note that the subarrays are disjoint if and only if there is no index k such that nums[k] belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.

'''
>>> s = Solution()
>>> s.canChoose([[1,-1,-1],[3,-2,0]], [1,-1,0,1,-1,-1,3,-2,0])
True
>>> s = Solution()
>>> s.canChoose([[10,-2],[1,2,3,4]], [1,2,3,4,10,-2])
False
>>> s = Solution()
>>> s.canChoose([[1,2,3],[3,4]], [7,7,1,2,3,4,7,7])
False

'''


class Solution:
    def canChoose(self, groups, nums) -> bool:
        i = 0
        for j in groups:
            while i < len(nums):
                if j == nums[i:i + len(j)]:
                    i += len(j)
                    break
                i += 1
            else:
                return False
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
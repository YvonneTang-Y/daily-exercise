# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

'''
>>> s = Solution()
>>> s.findMedianSortedArrays([1,3], [2])
2.0
>>> s = Solution()
>>> s.findMedianSortedArrays([1,2], [3,4])
2.5
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1 += nums2
        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2.0
        else:
            return nums1[(len(nums1) - 1) // 2] / 1.0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
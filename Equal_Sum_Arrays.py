# You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

# In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

# Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

'''
>>> s = Solution()
>>> s.minOperations([1,2,3,4,5,6], [1,1,2,2,2,2])
3
>>> s = Solution()
>>> s.minOperations([1,1,1,1,1,1,1], [6])
-1
>>> s = Solution()
>>> s.minOperations([6,6], [1])
3
'''

class Solution:
    def minOperations(self, nums1, nums2):
        count = 0
        # if the sum of nums1 and nums2 are same, return 0
        if sum(nums1) == sum(nums2):
            return 0
        # if the sum of nums1 and nums2 are impossible to be same, return -1
        if len(nums1) > len(nums2) * 6 or len(nums2) > len(nums1) * 6:
            return -1
        # let nums2 always be the larger list
        if sum(nums1) > sum(nums2):
            nums1, nums2 = nums2, nums1
        
        dict1, dict2 = {}, {}
        for i in nums1:
            dict1[i] = dict1.get(i, 0) + 1
        for i in nums2:
            dict2[i] = dict2.get(i, 0) + 1

        sum1 = sum(nums1)
        sum2 = sum(nums2)
        # choose the most difference element to be changed
        while sum1 != sum2:
            if 6 - min(dict1.keys()) >= max(dict2.keys()) - 1:
                if sum2 - sum1 <= 6 - min(dict1.keys()):
                    count += 1
                    return count
                else:
                    sum1 += 6 - min(dict1.keys())
                    if dict1[min(dict1.keys())] == 1:
                        del dict1[min(dict1.keys())]
                    else:
                        dict1[min(dict1.keys())] = dict1.get(min(dict1.keys())) - 1
                    dict1[6] = dict1.get(6, 0) + 1
                    count += 1
            else:
                if sum2 - sum1 <= max(dict2.keys()) - 1:
                    count += 1
                    return count
                else:
                    sum2 -= max(dict2.keys()) - 1
                    if dict2[max(dict2.keys())] == 1:
                        del dict2[max(dict2.keys())]
                    else:
                        dict2[max(dict2.keys())] = dict2.get(max(dict2.keys())) - 1
                    dict2[1] = dict2.get(1, 0) + 1
                    count += 1
        return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
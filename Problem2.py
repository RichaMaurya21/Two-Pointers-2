## Problem2 (https://leetcode.com/problems/merge-sorted-array/)
class Solution:
    def merge(self, nums1, m, nums2, n):
        p1 = m-1
        p2 = n-1
        idx = m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[idx] = nums2[p2]
                p2 -= 1

            idx -= 1

        while p2 >= 0:
            nums1[idx] = nums2[p2]
            p2 -= 1
            idx -= 1

        return nums1
        """
        Do not return anything, modify nums1 in-place instead.
        """

sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(sol.merge(nums1, m, nums2, n))
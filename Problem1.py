## Problem1 (https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        index = 2  # Start from the third position

        for i in range(2, len(nums)):
            # If the current number is not the same as the number at index - 2, it means we can keep it.
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1

        return index




sol = Solution()
nums = [1,1,1,2,2,3]
print(sol.removeDuplicates(nums))
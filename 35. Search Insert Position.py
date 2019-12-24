class Solution:
    def searchInsert(self, nums: [], target: int) -> int:
        for x,y in enumerate(nums):
            if y == target:
                return x
            elif y > target:
                return x
        return len(nums)
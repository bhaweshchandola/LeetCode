class Solution:
    def findPeakElement(self, nums: []) -> int:
        peak = []
        
        if len(nums) > 2:
            for x in range(1,len(nums)-1):
                if nums[x-1]<nums[x]>nums[x+1]:
                    peak.append(nums[x])
        
        print(nums)
        print(peak)
        print(len(peak))
        # print(peak[0])
        if len(peak) == 0:
            print("first")
            return nums.index(max(nums))
        else:
            print("second")
            return nums.index(peak[0])
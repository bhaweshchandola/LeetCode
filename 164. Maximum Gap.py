class Solution:
    def maximumGap(self, nums: []) -> int:
        if len(nums) < 2:
            return 0
        x = sorted(nums)
        max_c = -99
        for x1 in range(len(x)-1):
            diff_c = x[x1+1] - x[x1]
            if diff_c > max_c:
                max_c = diff_c
            
        return max_c
        
from collections import Counter 
class Solution:
    def majorityElement(self, nums: []) -> int:
        x = Counter(nums)
        return max(x, key=x.get)
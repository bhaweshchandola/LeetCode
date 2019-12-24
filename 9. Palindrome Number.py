class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        x2 = x1[::-1]
        
        if x1 == x2:
            return True
        else:
            return False
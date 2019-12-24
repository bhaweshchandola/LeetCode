class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        temp = 0
        if '-' in x:
            x.remove('-')
            temp = -int("".join(x[::-1]))
        else:
            temp = int("".join(x[::-1]))    
        if -2**31<temp< (2**31)-1:
            return temp
        else:
            return 0
        
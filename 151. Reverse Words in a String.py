class Solution:
    def reverseWords(self, s: str) -> str:
        x = " ".join(list(filter(None, s.split(' ')))[::-1])
        return x
        
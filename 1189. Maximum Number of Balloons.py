class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        
        fin = dict(Counter(text))
        x = []
        y = list("balloon")
        
        print(fin)
        for x1 in y:
            try:
                x.append(fin[x1])
                fin[x1] = fin[x1]//2
            except:
                return 0
        print(fin)
        print(x)
        return min(x)
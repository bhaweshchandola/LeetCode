class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        
        ver1 = list(map(int, ver1))
        ver2 = list(map(int, ver2))
        
        flag1 = 0
        flag2 = 0
        
        res = -2
        print(ver1)
        print(ver2)
        
        las1 = 0
        las2 = 0
        
        while res == -2:
            if (las1 or las2) == 1:
                if sum(ver1) > sum(ver2):
                    res = 1
                elif sum(ver1) < sum(ver2):
                    res = -1
                else:       
                    res = 0
                break
            if ver1[flag1] > ver2[flag2]:
                res = 1
                print("first", res)
                
                break
            elif ver1[flag1] < ver2[flag2]:
                res = -1
                print("second", res)
                break
                
            elif las1 == las2 == 1:
                if sum(ver1) > sum(ver2):
                    res = 1
                elif sum(ver1) < sum(ver2):
                    res = -1
                else:       
                    res = 0
                break
                
            
                
            if len(ver1) > flag1+1:
                flag1 += 1
            else:
                las1 = 1
            if len(ver2) > flag2+1:
                flag2 += 1
            else:
                las2 = 1
        
        return res
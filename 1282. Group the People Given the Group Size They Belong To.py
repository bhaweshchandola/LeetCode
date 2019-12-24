from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: []) -> [[]]:
        g = defaultdict(list)
        
        for ind, i in enumerate(groupSizes):
            g[i].append(ind)
            
        fin = []
        print(g)
        for x,y in g.items():
            coun = x
            temp = y
            print("coun, temp",coun, temp)
            if coun<len(temp):
                while coun<=len(temp):
                    print(temp)
                    fin.append(temp[:coun])
                    try:
                        temp = temp[coun:]
                    except:
                        temp = []
            else:
                fin.append(y)
                
        return fin
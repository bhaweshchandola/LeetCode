class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        if len(s) == 0:
            return True
        fin_ls = []
        for x in s:
            if x in ['[', '{', '(']:
                fin_ls.append(x)
            else:
                if len(fin_ls)>0:
                    if x == ']' and fin_ls[-1] == '[':
                        del fin_ls[-1]
                    elif x == '}' and fin_ls[-1] == '{':
                        del fin_ls[-1]
                    elif x == ')' and fin_ls[-1] == '(':
                        del fin_ls[-1]
                    else:
                        return False
                else:
                    return False
        if len(fin_ls) != 0:
            return False
        else:
            return True
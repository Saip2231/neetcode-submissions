class Solution:
    def calPoints(self, ops: List[str]) -> int:
        x = []
        for i in ops:
            if i not in ["+","C","D"]:
                x.append(int(i))
            elif i == "+":
                x.append(int(x[-1]) + int(x[-2]))
            elif i == "D":
                x.append(int(x[-1]) * 2)
            else:
                x.pop(-1)
        return(sum(x))
        
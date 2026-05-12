class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        res , resLen = [-1,-1] , float(9999)
        left = 0
        window , countT = {} , {}
        for c in t:
            countT[c] = 1+countT.get(c , 0)
        have , need = 0 , len(countT)
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have+=1

            while have == need:
                if(r-left+1)< resLen:
                    res = [left,r]
                    resLen = (r-left+1)
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -=1
                left = left + 1

        left,r = res
        return s[left:r+1] if resLen != float(9999) else ""



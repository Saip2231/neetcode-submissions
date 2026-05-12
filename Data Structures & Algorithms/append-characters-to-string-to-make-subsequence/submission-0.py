class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left,right = 0,0
        while(left<len(s) and right<len(t)):
            if s[left] == t[right]:
                left +=1 
                right+=1
            else:
                left+=1
        # print(left,right)
        return(len(t)-right)
        
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)>1:
            pointer = len(s)-1
            count =0
            while s[pointer] == ' ':
                pointer-=1
            while s[pointer] != ' ' and pointer:
                count+=1
                pointer-=1
            return count
        else:
            return 1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        start,end = 0 , len(s)-1
        while(start<end):
            if s[start] != s[end]:
                str1 = s[:start] + s[start+1:]
                str2 = s[:end] + s[end+1:]
                if str1 == str1[::-1] or str2 == str2[::-1]:
                    return True 
            start+=1
            end-=1
        return False
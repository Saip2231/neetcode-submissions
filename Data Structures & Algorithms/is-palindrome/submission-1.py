class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        left = 0
        right = len(s)-1
        while(right > 0 and left < len(s)):
            if(s[right].isalnum() == False):
                right = right -1
            if(s[left].isalnum() == False):
                left = left +1
            
            if s[right]!=s[left]:
                return False
            right = right -1
            left = left+1
                
        return True
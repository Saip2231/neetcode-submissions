class Solution:
    def scoreOfString(self, s: str) -> int:
        left,right = 0,1
        sum = 0
        while(left<right and right<len(s)):
            # print(s[left])
            sum += abs(ord(s[left]) - ord(s[right]))
            left+=1
            right+=1
        return (sum)
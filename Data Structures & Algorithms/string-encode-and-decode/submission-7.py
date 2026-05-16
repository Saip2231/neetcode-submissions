class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for word in strs:
            new_string += str(len(word)) + '#' + word
        return(new_string)

    def decode(self, s: str) -> List[str]:
        ans,i= [],0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1 
            length = int(s[i:j])
            ans.append(s[j+1:j+length+1])
            i=j+length+1
        return(ans)


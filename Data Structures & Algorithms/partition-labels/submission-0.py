class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i,c in enumerate(s):
            hashmap[c] = i
        output = []
        size , end = 0 , 0
        for i , c in enumerate(s):
            size+=1
            end = max(end,hashmap[c])
            
            if i == end:
                output.append(size)
                size = 0
        return output
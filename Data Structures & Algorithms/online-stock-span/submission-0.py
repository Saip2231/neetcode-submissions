class StockSpanner:
    def __init__(self):
        self.stack = []
        self.idx = -1 

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.idx +=1
        while self.stack and self.stack[-1][0]<=price: 
            self.stack.pop()
        ans = self.idx - (-1 if len(self.stack) == 0 else self.stack[-1][1])
        self.stack.append((price , self.idx))
        return ans

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
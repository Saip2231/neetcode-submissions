class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for x,y in points:
            dist = self.distance(x,y)
            # print(dist)
            heapq.heappush(res, (-dist, x, y))
            if len(res) > k:
                heapq.heappop(res)
        return [[x,y] for (_,x,y) in res]
        



    def distance(self,x, y):
        return math.sqrt(x**2 + y**2)



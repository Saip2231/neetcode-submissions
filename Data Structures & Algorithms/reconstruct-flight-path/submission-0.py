from collections import defaultdict
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        adj = defaultdict(list)

        # build a min-heap for each airport (lexicographically smallest popped first)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        def dfs(src):
            # always choose the smallest lexical destination first
            while adj[src]:
                next_dst = heapq.heappop(adj[src])
                dfs(next_dst)
            res.append(src)

        dfs("JFK")

        # reverse because Hierholzer builds the path backwards
        return res[::-1]
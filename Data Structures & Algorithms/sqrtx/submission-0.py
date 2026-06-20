class Solution:
    def mySqrt(self, x: int) -> int:
        start,end = 0,x
        res = 0
        while start<= end:
            mid = start+((end - start)//2)
            if mid**2 > x:
                end = mid-1
            elif mid**2 < x:
                start = mid+1
                res = mid
            else:
                return mid
        return(res)


class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        start, destination = sorted([start, destination])
        a = sum(distance[start:destination])
        b = sum(distance[destination:]+ distance[:start])
        # print(a,b)
        return min(a,b)

so = Solution()

print(so.distanceBetweenBusStops([1,2,3,4], 0,1))
print(so.distanceBetweenBusStops([1,2,3,4], 0,2))
print(so.distanceBetweenBusStops([1,2,3,4], 0,3))
print(so.distanceBetweenBusStops([7,10,1,12,11,14,5,0], 7,2))



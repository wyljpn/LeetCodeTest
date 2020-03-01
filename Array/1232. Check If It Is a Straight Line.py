class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        try:
            slope = (coordinates[1][1] -coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            for i in range(2, len(coordinates)):

                    if slope != (coordinates[i][1] -coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]):
                        return False
        except:
            return False

        return True


so = Solution()

print(so.checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))
print(so.checkStraightLine([[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]))
print(so.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(so.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(so.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
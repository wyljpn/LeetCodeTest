class Solution:
    def findMinArrowShots(self, points):

        points.sort(key=lambda x: x[0])

        result = 1

        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:
                result += 1
            else:
                points[i][1] = min(points[i][1], points[i-1][1])

        return result

if __name__ == "__main__":
    so = Solution()
    print(so.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(so.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(so.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
    print(so.findMinArrowShots([[-2147483648,2147483647]]))
    print(so.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
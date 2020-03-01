class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        soldiers = []

        for row in mat:
            soldiers.append(sum(row))

        res = []
        sorted_soldiers = sorted(soldiers)
        # print(soldiers)
        # print(sorted_soldiers)
        for i in range(k):
            weak_row = soldiers.index(sorted_soldiers[i])
            res.append(weak_row)
            soldiers[weak_row] = -i - 1
        # print(soldiers)
        return res

    # https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/discuss/496713/Python-One-Liner-using-Sorting
    def kWeakestRows_1(self, mat, k):
        # 拿sum(mat[x])来比较大小，实际存储的是key x
        # print(sorted(range(len(mat)), key=lambda x: sum(mat[x])))
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]


    def kWeakestRows_2(self, mat, k):

        from heapq import heappushpop, heappush, heappop

        heap = []  # Size: O(k)

        # Iterate over the rows in O(m).
        for index, row in enumerate(mat):
            soldier_count = self.soldier_count(row)

            # Push values to the heap in O(log k)
            # Heaps in Python will pop the smallest values first. Therefore we need to push tuples with inverted values onto our heap.
            if len(heap) == k:
                heappushpop(heap, (-soldier_count, -index))
            else:
                heappush(heap, (-soldier_count, -index))

        weakest_rows = []  # Size: O(k)

        # Push the heap values into our result list in O(k log k).
        while heap:
            weakest_rows.append(-heappop(heap)[1])

        # Return the result in reversed order.
        return weakest_rows[::-1]

        # Find the number of soldiers in a row using Binary Search in O(log n).

    def soldier_count(self, row):
        low, high = 0, len(row) - 1

        while low < high:
            mid = (low + high + 1) // 2

            if not row[mid]:
                high = mid - 1
            else:
                low = mid

        # We need to return a count and not an index.
        # Therefore we need to increase the result by one if soldiers have been found.
        if row[0]:
            low += 1

        return low



so = Solution()

# print(so.kWeakestRows([[1, 1, 0, 0, 0],
#                        [1, 1, 1, 1, 0],
#                        [1, 0, 0, 0, 0],
#                        [1, 1, 0, 0, 0],
#                        [1, 1, 1, 1, 1]], 3))
#
# print(so.kWeakestRows([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0]], 3))
#
# print(so.kWeakestRows([[1, 0, 0, 0],
#                        [1, 1, 1, 1],
#                        [1, 0, 0, 0],
#                        [1, 0, 0, 0]], 2))


print(so.kWeakestRows_1([[1, 1, 0, 0, 0],
                         [1, 1, 1, 1, 0],
                         [1, 0, 0, 0, 0],
                         [1, 1, 0, 0, 0],
                         [1, 1, 1, 1, 1]], 3))

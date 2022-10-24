class Solution:
    def findItinerary(self, tickets):

        from collections import defaultdict

        # key: 出发站
        # value：到达站
        ticketsDict = defaultdict(list)

        for item in tickets:
            ticketsDict[item[0]].append(item[1])

        for airport in ticketsDict:
            ticketsDict[airport].sort()

        def backtracking(startPoint):
            if len(path) == len(tickets) + 1:
                return True

            for _ in ticketsDict[startPoint]:
                endPoint = ticketsDict[startPoint].pop(0)
                path.append(endPoint)
                if backtracking(endPoint):
                    return True
                path.pop()
                ticketsDict[startPoint].append(endPoint)

        path = ["JFK"]
        backtracking(path)

        return path
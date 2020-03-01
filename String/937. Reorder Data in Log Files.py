class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letterList = []
        numberList = []
        for log in logs:
            logList = log.split(" ")
            if logList[1].isdigit():
                numberList.append(log)
            else:
                letterList.append((logList[0], " ".join(logList[1:])))
        letterList.sort(key=lambda x:x[1])
        resultList = [" ".join(a) for a in letterList]
        return resultList+numberList


    def reorderLogFiles_1(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)
        return sorted(logs, key = f)

    def reorderLogFiles_2(self, logs):
        l = filter(lambda l: l[l.find(" ") +1].isalpha(), logs)
        d = filter(lambda l: l[l.find(" ") +1].isdigit(), logs)
        return sorted(l, key=lambda x:(x[x.find(" "):], x[:x.find(" ")])) +list(d)


so = Solution()

print(so.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(so.reorderLogFiles_1(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
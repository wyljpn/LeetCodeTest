class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for elem in arr:
            dic[elem*2] = dic.get(elem*2, 0) + 1
        print(dic)

        for elem in arr:
            double_elem = dic.get(elem, -1)
            if elem == 0:
                if dic.get(elem, -1)==2:
                    return True
            elif double_elem != -1:
                return True
        return False

    def checkIfExist_1(self, arr):
        seen = set()
        for elem in arr:
            if elem *2 in seen or elem % 2 == 0 and elem /2 in seen:
                return True
            seen.add(elem)
        return False


so = Solution()

print(so.checkIfExist([10,2,5,3]))
print(so.checkIfExist([7,1,14,11]))
print(so.checkIfExist([3,1,7,11]))
print(so.checkIfExist([-2,0,10,-19,4,6,-8]))
print(so.checkIfExist([0,0]))
print(so.checkIfExist([-2,0,10,-19,4,6,-8]))
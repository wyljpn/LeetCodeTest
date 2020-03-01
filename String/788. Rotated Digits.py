class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        numb = set(['6', '9', '2', '5', '1', '0', '8'])

        cnt = 0
        for i in range(1, N+1):
            t = set(str(i))
            if t - numb == set():
                if t-set(['0', '1', '8']) ==set():
                    pass
                else:
                    cnt +=1
        return cnt
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        carry = 0
        K_len = len(str(K))
        A_len = len(A)
        i=0
        for i in range(K_len):
            # print("K1", K)
            residue = K % 10
            K //= 10
            # print("K2", K)
            # print("residue",residue)
            # print("carry", carry)
            if i >= A_len:
                carry, tmp = divmod(residue+carry, 10)
                A.insert(0, tmp)
            else:
                carry, A[-i-1] = divmod(A[-i-1] + residue + carry, 10)
            # print(A)

        for j in range(i+2, len(A)+1):
            if carry==0:
                break
            carry, A[-j] = divmod(A[-j] + carry, 10)

        if carry == 1:
            A.insert(0, 1)
        return A

so = Solution()

print(so.addToArrayForm([1,2,0,0], 34))
print(so.addToArrayForm([2,7,4], 181))
print(so.addToArrayForm([2,1,5], 806))
print(so.addToArrayForm([9,9,9], 1))
print(so.addToArrayForm([0], 23))
print(so.addToArrayForm([6], 809))
print(so.addToArrayForm([7], 993))
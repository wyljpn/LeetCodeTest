class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                if i == len(bits):
                    return False
            else:
                i += 1
        return True

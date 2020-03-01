class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.','[.]')

    def defangIPaddr_1(self, address):
        import re
        return re.sub('\.', '[.]', address)
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        # if length differs or set of characters differ, return False directly
        # if A and B are equal, returns if we have at least 1 repetitive character in the list
        # if two list have more than 2 indices with different characters, return false
        # In the end check if the swap can happen
        
        if len(A) != len(B) or set(A) != set(B):
            return False

        if A == B:
            return len(A) - len(set(A))>=1
        else:
            indices = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter+=1
                    indices.append(i)
                if counter >2:
                    return False
            return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]
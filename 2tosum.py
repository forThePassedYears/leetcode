

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = int(a, 2), int(b, 2)
        return bin(a + b)[2:]


i = Solution()

print(i.addBinary('1010', '1011'))

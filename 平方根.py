

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        return int(pow(x, 1 / 2))


s = Solution()
print(s.mySqrt(1))

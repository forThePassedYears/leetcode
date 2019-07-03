# coding:utf-8


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        for i in digits:
            s += str(i)
        s = int(s) + 1
        return [int(x) for x in str(s)]


q = Solution()

l1 = [9]
l2 = [1, 2, 9]
l3 = [1, 9, 9]
l4 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
print(q.plusOne(l1))
print(q.plusOne(l2))
print(q.plusOne(l3))
print(q.plusOne(l4))

# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        n = 0
        m = nums.length
        while n < nums.length & &m > 0:
            if n = m:
                continue
            if nums[n] + nums[m] = target:
            result.append(n, m)
            n += 1
            m -= 1
        return result


nums = [2, 7, 11, 15]
target = 9

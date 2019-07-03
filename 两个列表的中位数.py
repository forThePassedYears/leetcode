# -*- coding: utf-8 -*-


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # z = 0
        # if nums1:
        #     if len(nums1) % 2 == 1:
        #         z = int(len(nums1) / 2)
        #         nums1_z = nums1[z]
        #     else:
        #         z1 = int(len(nums1) / 2) - 1
        #         z2 = int(len(nums1) / 2)
        #         z = (nums1[z1] + nums1[z2]) / 2

        # n = 0
        # if nums2:
        #     if len(nums2) % 2 == 1:
        #         q = int(len(nums2) / 2)
        #         n = nums2[q]
        #     else:
        #         z1 = int(len(nums2) / 2) - 1
        #         z2 = int(len(nums2) / 2)
        #         n = (nums2[z1] + nums2[z2]) / 2

        # return '中位数是 （%s + %s ）/2 = %s' % (z, n, (z + n) / 2)
        res = nums1 + nums2  # [1,2,3,4,5] 3   [7,8,9,10] 8.5  11.5/2  5.75
        res.sort()
        n = len(res) // 2
        return res[n] if len(res) % 2 == 1 else (res[n] + res[n - 1]) / 2


nums1 = [1, 2, 3, 4, 5]
nums2 = [7, 8, 9, 10]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))

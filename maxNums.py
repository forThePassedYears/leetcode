# class Solution:
#     def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # l = len(nums)  # 求列表长度
        # i = 0
        # sum = 0  # 和
        # MaxSum = nums[0]
        # while i < l:
        #     sum += nums[i]
        #     if sum > MaxSum:
        #         MaxSum = sum
        #     if sum < 0:
        #         sum = 0
        #     i += 1
        # return MaxSum

        # sum = 0
        # maxsum = nums[0]
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     if sum > maxsum:
        #         maxsum = sum
        #     if sum < 0:
        #         sum = 0
        # return maxsum


class Solution:
    def arrayMax(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


s = Solution()
print(s.arrayMax([2, -1, -3, 4, -1, 2, -1, -5, -4]))

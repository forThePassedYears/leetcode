class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        max_len = 0
        start = 0
        dic = {}

        for i in range(len(s)):

            if s[i] in dic and dic[s[i]] > start:
                start = dic[s[i]] + 1

            one_max = i - start
            dic[s[i]] = i

            max_len = max(max_len, one_max)

        return max_len


a = Solution()
b = a.lengthOfLongestSubstring(' ')
print(b)

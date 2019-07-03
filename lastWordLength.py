class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        for i in s[::-1].lstrip():
            if i != ' ':
                l.append(i)
            else:
                break

        return len(l)


m = Solution()
print(m.lengthOfLastWord("hello world"))
print(m.lengthOfLastWord("a "))

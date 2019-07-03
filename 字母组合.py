# -*- coding: utf-8 -*-


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = [i for i in digit2chars[digits[0]]]

        for i in digits[1:]:
            res = [m + n for m in res for n in digit2chars[i]]

        return res


if __name__ == '__main__':
    a = Solution()
    result = a.letterCombinations('23')
    print(len(result))
    print(result)

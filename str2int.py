# -*- coding: utf-8 -*-


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re

        result = re.findall(r'^[-+]?\d+', str.strip())

        result_2 = ""

        if result:
            result = result[0]
            if result[0] == '-' or result[0] == '+':
                result_2 = result[1:]
            else:
                result_2 = result
            result_2 = int(result_2)
            if result[0] == '-':
                return -result_2 if -result_2 >= -2**31 else -2**31
            else:
                return result_2 if result_2 <= 2**31 - 1 else 2**31 - 1
        return 0

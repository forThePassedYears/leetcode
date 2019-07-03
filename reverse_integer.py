# -*- coding: utf-8 -*-


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > -10 and x < 10:
            return x

        str_x = str(x)

        if str_x[0] == '-':
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
        else:
            str_x = str_x[::-1]
            x = int(str_x)

        return x if -2147483648 < x < 2147483647 else 0

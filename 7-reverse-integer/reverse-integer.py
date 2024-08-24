class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        signed = -1 if x < 0 else 1
        x = abs(x)
        while x:
            value = x % 10
            num = num * 10 + value
            x /= 10
        output = signed * num
        if output > 2 ** 31 - 1 or output < -(2 ** 31):
            return 0
        return output
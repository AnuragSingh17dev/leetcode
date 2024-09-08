class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num, exp, sign, dec = False, False, False, False
        for digit in s:
            if digit >= '0' and digit <= '9':
                num = True     
            elif digit == 'e' or digit == 'E':
                if exp or not num: 
                    return False
                else: 
                    exp, num, sign, dec = True, False, False, False
            elif digit == '+' or digit == '-':
                if sign or num or dec: 
                    return False
                else: 
                    sign = True
            elif digit == '.':
                if dec or exp: 
                    return False
                else: 
                    dec = True
            else: 
                return False
        return num
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "inf" or s == "-inf" or s == "+inf" or s == "-Infinity" or s == "infinity" or s == "INFINITY" or s == "+Infinity" or s == "Infinity" or s == "nan" or s == "-nan" or s == "+nan":
            return False
        try:
            x = int(s)
            return True
        except:
            try:
                float(s)
                return True
            except:
                return False
        else:
            return False
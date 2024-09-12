class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
            else:
                st.pop()
                if len(st) == 0:
                    st.append(i)
                else:
                    max_length = max(max_length, i - st[-1])
        return max_length
        
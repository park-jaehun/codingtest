class Solution(object):
    def isValid(self, s):
        stack = []
        table = {
            ")": "(",
            "}": "{",
            "]": "["

        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

        """
        :type s: str
        :rtype: bool
        """

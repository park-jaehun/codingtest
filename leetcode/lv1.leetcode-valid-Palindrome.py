class Solution(object):
    def isPalindrome(self, s):
        if s is None:
            return True
        result = []
        for li_s in s:
            if li_s.isalnum():
                result.append(li_s.lower())
        # 팰린드롬 여부 확인
        while len(result) > 1:
            if result.pop(0) != result.pop():
                return False
        return True

        """
        :type s: str
        :rtype: bool
        """

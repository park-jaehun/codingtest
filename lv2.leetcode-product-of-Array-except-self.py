class Solution(object):
    def productExceptSelf(self, nums):
        p = 1
        out = []
        for i in range(len(nums)):
            out.append(p)
            # 자기 자신 고정하고 왼쪽부터 곱셈
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            # 자기 자신 고정하고 오른쪽부터
            p = p * nums[i]
        return out
        """
        :type nums: List[int]
        :rtype: List[int]
        """

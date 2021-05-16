class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    ls = [i, j]
                    return ls

            ##(1) 브루트 포스로 계산

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

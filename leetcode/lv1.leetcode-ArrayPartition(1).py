class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        result = []
        for i in range(0, len(nums), 2):
            result.append(min(nums[i], nums[i + 1]))
        return (sum(result))

        """
        :type nums: List[int]
        :rtype: int
        """

class Solution(object):
    def maxProfit(self, prices):
        min_price = sys.maxsize
        # 최대값 초기화, 최소값 초기화  = -sys.maxsize, sys_maxsize
        profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit

        """
        :type prices: List[int]
        :rtype: int
        """

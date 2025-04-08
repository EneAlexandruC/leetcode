class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                profit += prices[i + 1] - prices[i]
        return profit

def main():
    s = Solution
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))

if __name__ == '__main__':
    main()
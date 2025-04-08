class Solution:
   def maxProfit(self, prices: list[int]) -> int:
        best_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            best_price = min(best_price, prices[i])
            profit = max(profit, prices[i] - best_price)

        return profit
    

def main():
   s = Solution()
   prices = [7,1,5,3,6,4]
   print(s.maxProfit(prices))

if __name__ == '__main__':
   main()
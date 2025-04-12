class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start, tank = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        
        return start
    
        # FIRST TRY
        # n = len(cost)
        # for i in range(n):
        #     starting_gas = gas[i]
        #     if starting_gas == 0: 
        #         break
        #     tank = starting_gas
        #     for j in range(i, n + i):
        #         tank -= cost[j % n]
        #         if tank < 0:
        #             break
        #         elif j == n + i - 1 and tank + cost[j % n] >= starting_gas or tank + gas[(j + 1) % n] >= starting_gas:
        #             return i
        #         else:
        #             tank += gas[(j + 1) % n]
        #             if tank + gas[(j + 1) % n] >= starting_gas and j == n + i - 1:
        #                 return i
        # return -1
                
def main():
    s = Solution()
    gas = [5,8,2,8]
    cost = [6,5,6,6]
    print(s.canCompleteCircuit(gas,cost))

if __name__ == '__main__':
    main()
from collections import deque

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        g = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= g:
                g = i
        
        return True if g == 0 else False



def main():
    s = Solution()
    nums = [1]
    print(s.canJump(nums))

if __name__ == '__main__':
    main()
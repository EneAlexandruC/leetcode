class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps, left, right, farthest_jump = 0, 0, 0, nums[0]

        while right <= len(nums) - 1:
            for i in range(left, right + 1):
                if i >= len(nums):
                    break
                farthest_jump = max(farthest_jump, nums[i] + i)
            left = right + 1
            right = farthest_jump
            jumps += 1

        return jumps
                
def main():
    s = Solution()
    nums = [2,1]
    print(s.jump(nums))

if __name__ == '__main__':
    main()
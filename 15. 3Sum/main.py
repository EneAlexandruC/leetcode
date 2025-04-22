class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pairs = set()
        nums.sort()
        i, j, k = 0, 0, len(nums) - 1

        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    pairs.add((nums[i], nums[j], nums[k]))
                    j += 1
        return [list(pair) for pair in pairs]
        
def main():
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))

if __name__ == '__main__':
    main()
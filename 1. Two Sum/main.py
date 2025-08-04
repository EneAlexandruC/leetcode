class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # O(nlogn) solution
        i, j = 0, len(nums) - 1
        original = nums.copy()
        nums.sort()

        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        
        return [original.index(nums[i]), original.index(nums[j]) if nums[i] != nums[j] else original.index(nums[j], original.index(nums[i]) + 1)]
    
        # brute force solution O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

def main():
    s = Solution()
    print(s.twoSum([3,3], 6))

if __name__ == '__main__':
    main()
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        for j in range(i, len(nums)):
            if nums[j] == nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        return i

def main():
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))

if __name__ == '__main__':
    main()
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = defaultdict(int)

        for element in nums:
            freq[element] += 1
            if freq[element] > len(nums) // 2:
                return element

def main():
    s = Solution()
    nums = [3,2,3]
    print(s.majorityElement(nums))

if __name__ == '__main__':
    main()
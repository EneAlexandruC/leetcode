class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, right, min_terms, current_sum = 0, 0, 100001, 0

        while right < len(nums) or current_sum >= target:
            if current_sum < target and right < len(nums):
                current_sum += nums[right]
                right += 1
            else:
                if current_sum >= target:
                    min_terms = min((right - left), min_terms)
                current_sum -= nums[left]
                left += 1
        return 0 if min_terms == 100001 else min_terms

        # FIRST APPROACH
        # GOT TLE
        # window = 0
        # while window < len(nums):
        #     for i in range(len(nums) - window):
        #         if sum(nums[i:window + i + 1]) >= target:
        #             return window + 1
        #     window += 1
        # return 0

def main():
    s = Solution()
    print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))

if __name__ == '__main__':
    main()
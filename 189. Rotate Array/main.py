class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        aux = [0] * len(nums)
        k = k % len(nums)

        for i in range(len(nums)):
            aux[(k + i) % len(nums)] = nums[i]
        nums[:] = aux


def main():
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 9)
    print(nums)

if __name__ == '__main__':
    main()
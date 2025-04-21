class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        
        return [i + 1, j + 1]

        # TWO POINTERS APPROACH
        # index = 0
        # while numbers[index] <= target and index < len(numbers) - 1:
        #     index += 1
        
        # for i in range(index, 0, -1):
        #     for j in range(i - 1, -1, -1):
        #         if numbers[i] + numbers[j] == target:
        #             return [j + 1, i + 1]
        
        # for i in range(index + 1, len(numbers) - 1):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

def main():
    s = Solution()
    print(s.twoSum([-5,-3,0,2,4,6,8], 5))

if __name__ == '__main__':
    main()
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        _,  size = 0, len(nums)
        while _ < size:
            if nums[_] == val:
                size -= 1
                nums.remove(val)
                _ -= 1
            _ += 1
            
        return len(nums)
    
def main():
    sol = Solution()
    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    print("Test case 1:")
    print("Expected k = 2, got:", k1, "nums:", nums1)

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = sol.removeElement(nums2, val2)
    print("\nTest case 2:")
    print("Expected k = 5, got:", k2, "nums:", nums2)

if __name__ == '__main__':
    main()


import copy

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        aux = []

        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                aux.append(nums1[i])
                i += 1
            else:
                aux.append(nums2[j])
                j += 1
        
        while i < m:
            aux.append(nums1[i])
            i += 1

        while j < n:
            aux.append(nums2[j])
            j += 1

        nums1[:] = aux


def main():
    sol = Solution()

    # Test case 1: Normal case with overlapping elements
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(f"Test case 1 result: {nums1}")  # Expected: [1, 2, 2, 3, 5, 6]

    # Test case 2: nums1 is empty
    nums1 = [0, 0, 0]
    m = 0
    nums2 = [1, 2, 3]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(f"Test case 2 result: {nums1}")  # Expected: [1, 2, 3]

    # Test case 3: nums2 is empty
    nums1 = [1, 2, 3]
    m = 3
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    print(f"Test case 3 result: {nums1}")  # Expected: [1, 2, 3]

    # Test case 4: Both arrays are empty
    nums1 = []
    m = 0
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    print(f"Test case 4 result: {nums1}")  # Expected: []

    # Test case 5: nums1 has extra space but no initial elements
    nums1 = [0, 0, 0]
    m = 0
    nums2 = [2, 5, 6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(f"Test case 5 result: {nums1}")  # Expected: [2, 5, 6]

if __name__ == '__main__':
    main()
    
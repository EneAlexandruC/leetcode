class Solution:
    def maxArea(self, height: list[int]) -> int:
        max, left, area, right = 0, 0, 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            area = min(height[left], height[right]) * (right - left)
            if max < area:
                max = area
        
        return max

def main():
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))

if __name__ == '__main__':
    main()

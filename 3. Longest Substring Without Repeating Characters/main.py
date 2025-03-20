from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring, maxi = deque(), 0

        for index in range(len(s)):
            if s[index] not in substring:
                substring.append(s[index])
                maxi = max(maxi, len(substring))
            else:
                while s[index] in substring:
                    substring.popleft()
                substring.append(s[index])
        
        return maxi

def main():
    sol = Solution()
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "dvdf"
    print(sol.lengthOfLongestSubstring(s3))

if __name__ == '__main__':
    main()
                
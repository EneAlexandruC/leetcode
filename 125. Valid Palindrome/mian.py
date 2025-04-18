class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for char in s:
            if char.isalnum():
                filtered += char.lower()
        i, j = 0, len(filtered)
        n = (len(filtered) // 2) if len(filtered) % 2 == 0 else (len(filtered) // 2 + 1)
        while i < n:
            if filtered[i] != filtered[j]:
                return False
            i, j = i + 1, j - 1
        return True

def main():
    s = Solution()
    print(s.isPalindrome("......a....."))

if __name__ == '__main__':
    main()
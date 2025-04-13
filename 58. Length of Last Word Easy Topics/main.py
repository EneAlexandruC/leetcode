class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

def main():
    s = Solution()
    str = "   fly me   to   the moon  "
    print(s.lengthOfLastWord(str))

if __name__ == '__main__':
    main()
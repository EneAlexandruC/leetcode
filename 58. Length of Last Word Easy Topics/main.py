class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        letters = 0

        for word in words:
            letters = max(letters, len(word))
        
        return letters

def main():
    s = Solution()
    str = "   fly me   to   the moon  "
    print(s.lengthOfLastWord(str))

if __name__ == '__main__':
    main()
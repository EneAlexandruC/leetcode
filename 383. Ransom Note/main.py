class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        ransom_count = {}
        
        for i in range(len(magazine)):
            if magazine[i] in magazine_count:
                magazine_count[magazine[i]] += 1
            else:
                magazine_count[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in ransom_count:
                ransom_count[ransomNote[i]] += 1
            else:
                ransom_count[ransomNote[i]] = 1

        for char, count in ransom_count.items():
            if magazine_count.get(char, 0) < count:
                return False
        return True

def main():
    s = Solution()
    print(s.canConstruct("aa", "aab"))

if __name__ == '__main__':
    main()
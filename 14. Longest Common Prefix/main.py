class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_word = " " * 201
        matching_characters = 0
        
        for s in strs:
            if len(s) < len(min_word):
                min_word = s
        strs.remove(min_word)

        for i in range(len(min_word)):
            for j in range(len(strs)):
                if strs[j][i] != min_word[i]:
                    return min_word[:matching_characters]
            matching_characters += 1
        return min_word

    
def main():
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flower","flower","flower"]))


if __name__ == '__main__':
    main()
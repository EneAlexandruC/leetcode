from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        word_to_char = {}

        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in char_to_word:
                char_to_word[pattern[i]] = i
            if words[i] not in word_to_char:
                word_to_char[words[i]] = i
            if char_to_word[pattern[i]] != word_to_char[words[i]]:
                return False
        return True


def main():
    s = Solution()
    print(s.wordPattern("abba", "dog dog cat dog"))

if __name__ == '__main__':
    main()
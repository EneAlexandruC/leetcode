from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_index = defaultdict(str)
        s_index = defaultdict(str)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            t_index[t[i]] += "+"
            s_index[s[i]] += "+"
        
        for i in range(len(s)):
            if t_index[s[i]] != s_index[s[i]]:
                return False
        return True
def main():
    s = Solution()

if __name__ == '__main__':
    main()
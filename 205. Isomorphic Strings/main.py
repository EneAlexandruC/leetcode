class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sindex = {}
        tindex = {}

        for i in range(len(s)):
            if s[i] not in sindex:
                sindex[s[i]] = i
            if t[i] not in tindex:
                tindex[t[i]] = i
            if sindex[s[i]] != tindex[t[i]]:
                return False

        return True
def main():
    s = Solution()
    print(s.isIsomorphic('code', 'leet'))

if __name__ == '__main__':
    main()
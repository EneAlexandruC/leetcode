class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spointer = tpointer = 0

        while spointer < len(s) or tpointer < len(t):
            if s[spointer] == t[tpointer]:
                tpointer += 1
            spointer += 1
        
        return tpointer == len(t)
    
        # FIRST APPROACH
        # index, count = 0 , 0
        # for i in range(len(t)):
        #     if t[i] == s[index]:
        #         for j in range(i, len(t)):
        #             if t[j] == s[index]:
        #                 index, count = index + 1, count + 1
        #         if count == len(s):
        #             return True
        #         else:
        #             return False
        # return True if len(s) == 0 else False

def main():
    s = Solution()
    print(s.isSubsequence("axc", "ahbgdc"))

if __name__ == '__main__':
    main()
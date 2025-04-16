class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # SLICING METHOD
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle) + i] == needle:
                return i
        return -1

        #FIRST APPROACH
        if len(haystack) < len(needle):
            return -1
        
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                flag = True
                for j in range(len(needle)):
                    if needle[j] != haystack[i + j] or i + j > len(haystack) - 1:
                        flag = False
                        break
                if flag:
                    return i
        return -1
    
def main():
    s = Solution()
    print(s.strStr("aaa", "aaa"))

if __name__ == '__main__':
    main()
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        map = {i: "" for i in range(numRows)}
        index, switch, ans = 0, True, ""

        if numRows <= 1:
            return s

        for i in range(len(s)):
            if index == numRows - 1 or index == 0:
                switch = not switch
            map[index] += s[i]
            index = index - 1 if switch else index + 1

        for i in range(numRows):
            ans += map[i]

        return ans



def main():
    s = Solution()
    print(s.convert("AB", 1))

if __name__ == '__main__':
    main()
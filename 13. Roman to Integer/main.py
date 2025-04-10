class Solution:
    def romanToInt(self, s: str) -> int:
        rtn = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = 0
        i = len(s) - 1
        while i >= 0:
            if i > 0:
                if (s[i] == "V" or s[i] == "X") and s[i - 1] == "I":
                    n += 4 if s[i] == "V" else 9
                    i -= 2
                    continue
                elif (s[i] == "L" or s[i] == "C") and s[i - 1] == "X":
                    n += 40 if s[i] == "L" else 90
                    i -= 2
                    continue
                elif (s[i] == "D" or s[i] == "M") and s[i - 1] == "C":
                    n += 400 if s[i] == "D" else 900
                    i -= 2
                    continue
            n += rtn[s[i]]
            i -= 1
        return n
def main():
    s = Solution()
    str = "MCMXCIV"
    print(s.romanToInt(str))

if __name__ == '__main__':
    main()
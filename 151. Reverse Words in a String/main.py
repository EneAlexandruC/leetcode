class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
    
        # FIRST APPROACH
        # words = s.split()
        # ans = ""

        # for i in range(len(words) - 1, -1, -1):
        #     ans += words[i] + " "

        # return ans[:len(ans) - 1]

def main():
    raise NotImplemented

if __name__ == '__main__':
    main()
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}

        def get_next_number(n: int) -> int:
            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n //= 10
            return result

        while n != 1:
            if n in visited:
                return False
            else:
                visited[n] = 1
            n = get_next_number(n)
        
        return True

def main():
    s = Solution()
    print(s.isHappy(2))

if __name__ == '__main__':
    main()
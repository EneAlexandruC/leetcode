class Solution:
    def hIndex(self, citations: list[int]) -> int:
        freq = [0] * (len(citations) + 1)
        cumulative_papers = 0

        for i in range(len(citations)):
            if citations[i] > len(citations):
                freq[-1] += 1
            else:
                freq[citations[i]] += 1
        
        for i in range(len(citations), -1, -1):
            cumulative_papers += freq[i]
            if cumulative_papers >= i:
                return i
        

def main():
    raise NotImplemented

if __name__ == '__main__':
    main()
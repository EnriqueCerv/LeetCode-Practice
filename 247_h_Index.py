class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for idx, cites in enumerate(citations):
            if cites < idx + 1:
                return idx
        
        return len(citations)
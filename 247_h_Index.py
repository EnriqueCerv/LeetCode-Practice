
# %% 274 h index
def hIndex(citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_index = 0
        citations.sort()
        citations.reverse()
        min_citations = citations[0]
        for i in range(len(citations)):
            min_citations = min(min_citations, citations[i])
            if i+1 <= min_citations:
                h_index += 1
        return h_index

def hIndex(citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        hIndex = 0
        citations.sort()
        citations.reverse()

        for citation in citations:
            if citation > hIndex:
                hIndex += 1
        return hIndex
citations = [3,0,6,1,5]
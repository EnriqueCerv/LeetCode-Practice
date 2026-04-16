class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def hamming_dist(word1, word2):
            return sum(1 for i in range(len(word1)) if word1[i] != word2[i])
        
        from collections import deque
        queue = deque([beginWord])
        steps = 0
        seen = set(beginWord)

        while queue:
            steps += 1

            for _ in range(len(queue)):
                cur_word = queue.popleft()
                if cur_word == endWord:
                    return steps
                
                for idx, next_word in enumerate(wordList):
                    if hamming_dist(cur_word, next_word) == 1 and next_word not in seen:
                        queue.append(next_word)
                        seen.add(next_word)
        
        return 0


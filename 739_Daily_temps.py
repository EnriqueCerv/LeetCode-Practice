class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):

            while stack and stack[-1][-1] < temp:
                pop_idx, _ = stack.pop()
                answer[pop_idx] = idx - pop_idx
            
            stack.append((idx, temp))

        return answer

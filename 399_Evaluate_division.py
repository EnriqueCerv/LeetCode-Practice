class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict

        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))
        
        def dfs(cur_var, cum_weight, visited):
            nonlocal target_var
            # Base cases
            if cur_var == target_var:
                return cum_weight

            visited.add(cur_var)

            for new_var, weight in graph[cur_var]:
                if new_var not in visited:
                    result = dfs(new_var, cum_weight * weight, visited)
                    if result != -1:
                        return result

            return -1

        answers = []
        for c, d in queries:
            if c not in graph or d not in graph:
                answers.append(-1)
            else:
                target_var = d
                answers.append(dfs(c, 1, set()))
            
        return answers
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## Bellman-Ford
        dist = [0] * numCourses

        # Relax edges n-1 times
        for _ in range(numCourses - 1):
            updated = False
            for course, prereq in prerequisites:
                # edge: prereq -> course, weight = -1
                if dist[prereq] - 1 < dist[course]:
                    dist[course] = dist[prereq] - 1
                    updated = True
            if not updated:
                break

        # One more pass to detect cycle
        for course, prereq in prerequisites:
            if dist[prereq] - 1 < dist[course]:
                return False

        return True

        # from collections import defaultdict

        # graph = defaultdict(list)
        # for a, b in prerequisites:
        #     graph[a].append(b)

        ## DFS approach
        # def dfs(course):
        #     if course in stack:
        #         return True
        #     if course in visited:
        #         return False
            
        #     visited.add(course)
        #     stack.add(course)

        #     for prereq in graph[course]:
        #         if dfs(prereq):
        #             return True
            
        #     stack.remove(course)
        #     return False
        
        # visited = set()
        # stack = set()
        # for course in range(numCourses):
        #     if course not in visited:
        #         if dfs(course):
        #             return False
        # return True

        
        
        
        

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dist = [0] * numCourses
        pred = {i: None for i in range(numCourses)}

        for _ in range(numCourses - 1):
            updated = False
            for course, prereq in prerequisites:
                if dist[prereq] - 1 < dist[course]:
                    dist[course] = dist[prereq] - 1
                    pred[course] = prereq
                    updated = True
            
            if not updated:
                break
        
        for course, prereq in prerequisites:
            if dist[prereq] - 1 < dist[course]:
                return []
        
        def rec(course):
            if pred[course] is None:
                if course not in order:
                    order.append(course) 
            else:
                rec(pred[course])
                if course not in order:
                    order.append(course)

        order = []
        for course in range(numCourses):
            if course in order:
                continue
            else:
                rec(course)
        return order

        
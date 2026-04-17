# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # # dfs
        # max_depth = -1
        # result = []

        # def dfs(node, cur_depth):
        #     nonlocal max_depth

        #     if node is None:
        #         return
            
        #     if cur_depth > max_depth:
        #         max_depth = cur_depth
        #         result.append(node.val)
            
        #     dfs(node.right, cur_depth + 1)
        #     dfs(node.left, cur_depth + 1)
        
        # dfs(root, 0)
        # return result

        # bfs
        if root == None:
            return []
            
        from collections import deque

        result = []
        queue = deque([root])

        while queue:
            level = len(queue)

            for idx in range(level):
                node = queue.popleft()

                if idx == level - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

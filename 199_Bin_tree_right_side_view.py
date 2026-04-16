# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # # dfs
        # result = []
        # depth = -1

        # def dfs(node, cur_depth):
        #     nonlocal depth
        #     if node is None:
        #         return
        #     if cur_depth > depth:
        #         result.append(node.val)
        #         depth = cur_depth

        #     dfs(node.right, cur_depth + 1)
        #     dfs(node.left, cur_depth + 1)
        
        # dfs(root, 0)
        # return result

        # bsf
        from collections import deque
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = len(queue)

            for i in range(level):
                node = queue.popleft()
                if i == level - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
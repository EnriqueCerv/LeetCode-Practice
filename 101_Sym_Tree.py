def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            if not all([node1, node2]) or node1.val != node2.val:
                return False
            
            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        
        return dfs(root, root)

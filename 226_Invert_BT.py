def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(node):
            if node is None:
                return
            node.right, node.left = node.left, node.right
            rec(node.right)
            rec(node.left)
        
        rec(root)
        return root
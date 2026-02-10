def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = first = second = None
        def rec_trav(node):
            if node is None:
                return

            nonlocal prev, first, second

            rec_trav(node.left)

            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node
            
            prev = node

            rec_trav(node.right)
        
        rec_trav(root)
        first.val, second.val = second.val, first.val
        return root
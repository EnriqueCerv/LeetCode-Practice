# %%
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def toBstRec(left, right):
            if left > right:
                return None
            
            middle = (right + left) // 2

            left_SubTree = toBstRec(left, middle - 1)
            right_SubTree = toBstRec(middle + 1, right)

            return TreeNode(nums[middle], left_SubTree, right_SubTree)

        return toBstRec(0, len(nums) - 1)
# %%
nums = [-10,-3,0,5,9]
head = sortedArrayToBST(nums)
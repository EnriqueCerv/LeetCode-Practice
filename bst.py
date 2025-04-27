# %%
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST_Rec:
    def __init__(self):
        self.root = None


    def insert(self, value):
        self.root = self.insertRec(self.root, value)

    def insertRec(self, node, value):
        if node is None:
            return Node(value)
        if value >= node.val:
            if node.right is None:
                node.right = Node(value)
                return node
            self.insertRec(node.right, value)
        else:
            if node.left is None:
                node.left = Node(value)
                return node
            self.insertRec(node.left, value)

        # return node


    def search(self, value):
        return self.searchRec(self.root, value)

    def searchRec(self, node, value):
        if node is None:
            return 'Value does not exist, please insert first.'
        
        if node.val == value:
            return node
        
        if value > node.val:
            return self.searchRec(node.right, value)
        else:
            return self.searchRec(node.left, value)


    def traversal(self):
        arr = []
        self.traversalRec(self.root, arr)
        return arr

    def traversalRec(self, node, arr):
        if node is not None:
            self.traversalRec(node.left, arr)
            arr.append(node.val)
            self.traversalRec(node.right, arr)

    def getMin(self):
        return self.getMinRec(self.root)
    
    def getMinRec(self, node):
        if node.left is None:
            return self.val
        return self.getMin(node.left)


    def getMax(self):
        return self.getMinRec(self.root)
        
    def getMaxRec(self, node):
        if node.left is None:
            return self.val
        return self.getMin(node.left)


    def delete(self, value):
        return self.deleteRec(self.root, value)

    def deleteRec(self, node, value):
        if node is None:
            return 'Value does not exist, please insert first.'
        
        if value > node.val:
            return self.deleteRec(node.right, value)
        elif value < node.val:
            return self.deleteRec(node.left, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self.GetMin(node.right)
            node.key = min_larger_node.key
            node.right = self.deleteRec(node.right, min_larger_node.key)
        return node
# %%
# Iterative BST
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST_It:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        toInsert = Node(value)
        parent = None
        curr = self.root

        if curr is None:
            self.root = toInsert
            return self.root
        
        while curr is not None:
            parent = curr
            if value >= curr.val:
                curr = curr.right
            else:
                curr = curr.left
            
        if value >= parent.val:
            parent.right = toInsert
        else:
            parent.left = toInsert
        
        return self.root


    def getMin(self):
        curr = self.root
        if curr is None:
            return 'Tree empty'
        while curr is not None:
            min = curr.val
            curr = curr.left
        return min

    
    def getMax(self):
        curr = self.root
        if curr is None:
            return 'Tree Empty'
        while curr is not None:
            max = curr.val
            curr = curr.right
        return max
    

    def traversal(self):
        sortedArr = []
        self.traversalRec(self.root, sortedArr)
        return sortedArr

    def traversalRec(self, node, arr):
        if node is not None:
            self.traversalRec(node.left, arr)
            arr.append(node.val)
            self.traversalRec(node.right, arr)

    def delete(self, value):
        return self.deleteRec(self.root, value)
    
    def deleteRec(self, node, value):
        if node is None:
            return 'Value does not exist'

        if value > node.val:
            return self.deleteRec(node.right, value)
        elif value < node.val:
            return self.deleteRec(node.left, value)
        else:
            if node.left is None:
                node = node.right
                return node
            elif node.right is None:
                return node.left
            min_larger_node = self.GetMin(node.right)
            node.key = min_larger_node.key
            node.right = self.deleteRec(node.right, min_larger_node.key)
        return node
    


# %%
# Example usage
bst = BST_It()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

bst.getMax()
print(bst.traversal())
bst.delete(40)
print(bst.traversal())
# %%

# print("Inorder traversal:", bst.traversal())  # [20, 30, 40, 50, 60, 70, 80]

# print("Search for 40:", bst.search(40) is not None)  # True

# bst.delete(50)
# print("Inorder traversal after deleting 50:", bst.traversal())  # [20, 30, 40, 60, 70, 80]
# %%

# %%

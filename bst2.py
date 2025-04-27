#%%
class Node:
    def __init__(self, x):
        self.val = x
        self.l = None
        self.r = None
# %%
# Recursive BST

class Rec_BST:
    def __init__(self):
        self.root = None
    
    def insert(self, x):
        if self.root is None:
            self.root = self.insertRec(self.root, x)
        else: 
            self.insertRec(self.root, x)
        return self.root

    def insertRec(self, node, x):
        if node is None:
            return Node(x)
        elif x < node.val:
            if node.l is None:
                node.l = Node(x)
                return node
            self.insertRec(node.l, x)
        else:
            if node.r is None:
                node.r = Node(x)
                return node
            self.insertRec(node.r, x)

    def search(self, x):
        return self.searchRec(self.root, x)

    def searchRec(self, node, x):
        if not node:
            return 'value does not exist'
        elif x == node.val:
            return node
        elif x < node.val:
            return self.searchRec(node.l, x)
        else:
            return self.searchRec(node.r, x)

    def traversal(self):
        sorted_arr = []
        self.traversalRec(self.root, sorted_arr)
        return sorted_arr

    def traversalRec(self, node, arr):
        if node:
            self.traversalRec(node.l, arr)
            arr.append(node.val)
            self.traversalRec(node.r, arr)

    def getMin(self):
        node = self.getMinRec(self.root)
        return node, node.val

    def getMinRec(self, node):
        if node.l is None:
            return node
        return self.getMinRec(node.l)

    def getMax(self):
        node = self.getMaxRec(self.root)
        return node, node.val

    def getMaxRec(self, node):
        if node.r is None:
            return node
        return self.getMaxRec(node.r)
    
        
# %%
# Iterative BST

class Ite_BST():
    def __init__(self):
        self.root = None
    
    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return self.root
        else:
            curr = self.root
            while curr is not None:
                if x < curr.val:
                    if curr.l is None:
                        curr.l = Node(x)
                        return self.root
                    curr = curr.l
                else:
                    if curr.r is None:
                        curr.r = Node(x)
                        return self.root
                    curr = curr.r

    def search(self, x):
        curr = self.root

        while curr:
            if curr.val == x:
                return curr
            elif x < curr.val:
                curr = curr.l
            else:
                curr = curr.r
            
        return 'value does not exist'

        
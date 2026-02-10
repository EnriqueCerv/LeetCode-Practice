class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(cur_node):
            if cur_node is None:
                return None

            if cur_node in visited:
                return visited[cur_node]
            
            clone = Node(cur_node.val)
            visited[cur_node] = clone

            for neighbor in cur_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        visited = {}
        return dfs(node)
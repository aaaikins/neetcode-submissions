class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        visited = set()
        count = 0

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(node):
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    dfs(n)
            
        
        for node in graph:
            if node not in visited:
                visited.add(node)
                dfs(node)
                count += 1
            
        return count
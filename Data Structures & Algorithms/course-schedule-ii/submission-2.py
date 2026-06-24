from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        courseMap = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for crs, pre in prereqs:
            courseMap[pre].append(crs)
            in_degree[crs] += 1
        
        q = deque([c for c in range(numCourses) if in_degree[c] == 0])
        
        completed = []

        while q:
            cur = q.popleft()
            for neighbor in courseMap[cur]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
            completed.append(cur)

        return completed if len(completed) == numCourses else []

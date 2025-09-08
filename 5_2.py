import sys
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(200000)

class Solution:
    def findComponents(self, n, m, edges):
        graph = defaultdict(list)
        

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)

        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        

        components = []
        

        for i in range(1, n + 1):
            if not visited[i]:
                component = []
                dfs(i, component)
                components.append(component)

        print(len(components))
        for component in components:
            print(len(component))
            print(" ".join(map(str, component)))


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

solution = Solution()
solution.findComponents(n, m, edges)

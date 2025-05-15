from collections import deque

def bfs(graph, start, end, n):
    queue = deque([start])
    visited = [False] * n
    parent = [-1] * n
    visited[start] = True
    
    while queue:
        u = queue.popleft()
        
        if u == end:
            path = []
            while u != -1:
                path.append(u + 1)
                u = parent[u]
            path.reverse()
            return len(path) - 1, path
        
        for v in range(n):
            if graph[u][v] == 1 and not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    
    return -1, []

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start, end = map(int, input().split())

start -= 1
end -= 1

distance, path = bfs(graph, start, end, n)

if distance == -1:
    print(-1)
else:
    print(distance)
    print(" ".join(map(str, path)))

def dfs(graph, u, parent, visited, path, n):
    visited[u] = True
    path.append(u)
    
    for v in range(n):
        if graph[u][v] == 1:
            if not visited[v]:
                if dfs(graph, v, u, visited, path, n):
                    return True
            elif v != parent:
                cycle_start = v
                cycle = []
                while path:
                    cycle.append(path.pop())
                    if cycle[-1] == cycle_start:
                        break
                cycle.append(cycle_start)
                cycle.reverse()
                print("YES")
                print(len(cycle))
                print(" ".join(map(str, [x + 1 for x in cycle])))
                return True
    path.pop()
    return False

def find_cycle(graph, n):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            path = []
            if dfs(graph, i, -1, visited, path, n):
                return
    print("NO")

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

find_cycle(graph, n)

def dfs(maze, visited, x, y, n):
    if x < 0 or x >= n or y < 0 or y >= n or maze[x][y] == '*' or visited[x][y]:
        return 0
    visited[x][y] = True
    area = 1
    area += dfs(maze, visited, x + 1, y, n)
    area += dfs(maze, visited, x - 1, y, n)
    area += dfs(maze, visited, x, y + 1, n)
    area += dfs(maze, visited, x, y - 1, n)
    return area

n = int(input())
maze = [list(input().strip()) for _ in range(n)]
x, y = map(int, input().split())
x -= 1
y -= 1

visited = [[False] * n for _ in range(n)]

result = dfs(maze, visited, x, y, n)

print(result)

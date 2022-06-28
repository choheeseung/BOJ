from collections import deque

t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    result = 0

    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = 0
                bfs(graph, i, j)
                result += 1
    print(result)

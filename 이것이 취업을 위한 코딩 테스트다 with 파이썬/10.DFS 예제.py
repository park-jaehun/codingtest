# 자세한 문제 풀이 .....
# -*- coding: utf-8 -*-
# DFS 매서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]

]
visited = [False] * 9
dfs(graph, 1, visited)

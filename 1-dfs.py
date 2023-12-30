n=5
graph= [[1,3],[0],[4],[0],[2]]

visited= [False]*n

def dfs(u):
    visited[u] = True
    print('Visiting node: ',u)
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    print('Backing node: ',u)
    
for u in range(n):
    if not visited[u]:
        dfs(u)

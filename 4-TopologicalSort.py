#Name: Naimoon Jannat Prapti
#ID: 2157CSE00922

graph = [[2,6],[3],[3],[4,5],[5],[],[4]]

n = len(graph)
visited = [False]*n
topsort = []

def dfs(u):
    visited[u] = True
    print('Visiting Node: ',u)

    for v in graph[u]:
        if not visited[v]:
            dfs(v) 
    print('Backtracking Node: ',u)
    topsort.append(u)

dfs(0)
topsort.reverse()
print(topsort)

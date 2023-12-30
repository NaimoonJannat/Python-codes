n= 13
graph= [[1,9],[0,8],[3],[2,4,5,7],[3],[3,6],[5,7],[3,6,8,10,11],
        [1,7,9],[0,8],[7,11],[7,10],[]]

visited= [False]*n

def dfs(u):
    print('Visiting node: ',u)
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    print('Backing node: ',u)
    
def find_components():
    count= 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return count
print('The number of connected components are: ',find_components())



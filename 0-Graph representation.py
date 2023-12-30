#Adjacency Matrix
graph = [[0,1,1,0,0,1,0,0],
         [1,0,0,0,1,0,0,1],
         [1,0,0,0,0,0,0,0],
         [0,0,0,0,1,0,0,0],
         [0,1,0,1,0,0,0,0],
         [1,0,0,0,0,0,1,0],
         [0,0,0,0,0,1,0,0],
         [0,1,0,0,0,0,0,0]]
print("Graph from Adjacency Matrix: ")
for i in range(8):
    for j in range(8):
        if graph[i][j] == 1:
            print(i," --> ",j)


#Adajency List
graph = [[1,9],
         [0,8],
         [3],
         [2,4,5,7],
         [3],
         [3,6],
         [5,7],
         [3,6,8,10,11],
         [1,7,9],
         [0,8],
         [7,11],
         [7,10],
         []]
print("Graph from Adjacency List: ")
for u in range(len(graph)):
    for v in graph[u]:
        print(u,' --> ',v)

#Adjacency List for weighted graph

graph = [[(1,-1),(2,2),(5,1)],
         [(7,6)],
         [],
         [(4,3)],
         [(1,4)],
         [],
         [(5,2)],
         []]
print("Weighted Graph from Adjacency List: ")
for u in range(len(graph)):
    for v in graph[u]:
        print(u,' --> ',v[0],' cost: ',v[1])

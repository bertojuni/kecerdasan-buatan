vertexList = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
edgeList = [ (0,1),(1,2), (1,3), (1,4), 
			 (2,1), (2,5), (2,6), (3,1), (3,21), (3,8), (4,1), (4,9), (4,22),  
			 (5,2), (6,2), (6,23), (6,7), (21,3), (8,3), (8,10), (9,4), (22,4), 
			 (23,6), (7,6), (10,8)]
graphs = (vertexList, edgeList)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

 
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs, 1))
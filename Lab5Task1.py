graph={
    'A':['B','D'],
    'B': ['C', 'E'],
    'C': [],
    'D': ['G', 'H', 'E'],
    'E': ['C', 'F'],
    'F': [],
    'G': ['H'],
    'H': []
}

def bfs(graph,start,goal):
    queue=[(start,[start])]
    while queue:
        node,path=queue.pop(0)
        print("BFS Visiting Node: ",node)
        
        if node ==goal:
            return path
        
        for neighbours in graph[node]:
            if neighbours not in path:
                queue.append((neighbours,path +[neighbours]))
                
    return None


bfs_path=bfs(graph,'A','F')

if bfs_path:
    print("BFS: ",bfs_path)
else:
    print("Goal is not found")
    
def dfs(graph,start,goal):
    stack=[(start,[start])]
    while stack:
        node,path=stack.pop()
        print("DFS Visiting Node: ",node)
        if node==goal:
            return path
        
        for neighbors in graph[node]:
            if neighbors not in path:
                stack.append((neighbors,path+[neighbors]))
    return None
print()
dfs_path=dfs(graph,'A','F')
if dfs_path:
    print("Dfs: ",dfs_path)
    
else:
    print("not found in dfs")
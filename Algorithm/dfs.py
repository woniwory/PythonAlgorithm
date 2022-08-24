#2022_08_23 depth_first_search

def dfs(visited, v, graph):
  visited[v] = True
  for i in graph[v]:
    if visited[v] == False:
      dfs(v, visited, graph)
  
visited = [False] * 9  
graph = [
  [],
  [2,5,7],
  [1,3],
  [2,4],
  [3,5],
  [1,4],
  [8],
  [1,8],
  [6,7],
]


dfs(visited, 1, graph)

  

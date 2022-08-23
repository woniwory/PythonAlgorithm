#binary_search 2022_08_23

graph = [1,2,3,4,5,6,7,8,9,10]
target = 3

def binary_search(start, end, graph, target):
  mid = end // 2 
  if graph[mid] > target:
    binary_search(start, mid+1, graph, target)
  elif graph[mid] < target:
    binary_search(start, mid+1, graph, target)
  else:
    answer = graph[mid]
    print(answer) # 4. index에 주의할 것.
    
    
binary_search(1,10,graph,target)

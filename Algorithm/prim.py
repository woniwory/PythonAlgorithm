import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
visited = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
heap = [[0, 1]]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append([w, b])
    graph[b].append([w, a])

print(graph)
answer = 0
cnt = 0
while heap:
    if cnt == v:
        break
    w, a = heapq.heappop(heap)
    print(heap)
    if not visited[a]:
        visited[a] = True
        answer += w
        cnt += 1
        for i in graph[a]:
            heapq.heappush(heap, i)

print(answer)

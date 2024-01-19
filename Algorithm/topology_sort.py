import sys
from collections import deque

# 노드의 개수, 간선의 개수 입력 받기
v, e = map(int, sys.stdin.readline().split())

# 진입차수표( 노드의 수 +1 )
indegree = [0] * (v + 1)

# 노드 연결 정보 리스트( 노드의 수 +1 )
graph = [[] for _ in range(v + 1)]

# 간선 개수만큼 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # A -> B
    indegree [b] += 1  # 진입차수표도 하나씩 증가


# 위상 정렬 함수
def toplogy_sort():

    # 큐 구현
    queue = deque()
    result = []

    # 처음 시작 시 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree [i] == 0:
            queue .append(i)

    # 큐가 빌때까지 수행
    while queue :

        # 제일 왼쪽에 있는 큐를 pop
        now = queue .popleft()
        result.append(now)

        # now와 연결된 그래프
        for i in graph[now]:
            indegree[i] -= 1  # 1씩 제거
            # 진입차수가 0인 값은 큐에 다시 삽입
            if indegree[i] == 0:
                queue .append(i)

    for i in result:
        print(i, end=' ')

toplogy_sort()

#
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

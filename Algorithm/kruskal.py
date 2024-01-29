

# 특정 원소가 속한 집합을 찾기

def find_parent(parent, x):
    if parent[x] != x: #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



v = int(input())
e = int(input())
parent = [0] * (v+1)


edges = []
result = 0


for i in range(1, v+1):
    parent[i] = i



for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


edges.sort()


# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

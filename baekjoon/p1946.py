import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    list = []
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        list.append((a, b))
    list.sort(key= lambda x: x[0])
    tmp = list[0][1]
    cnt = 1
    for i in range(1, n):
        if list[i][1] < tmp:
            tmp = list[i][1] # 꼭 최신화해줄 것!!
            cnt = cnt + 1

    print(cnt)

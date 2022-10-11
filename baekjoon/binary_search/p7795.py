import sys

t = int(input())
answer = [0] * t

for testcase in range(t):
    
    n, m = map(int, sys.stdin.readline().split())
    nlist = sorted(list(map(int, sys.stdin.readline().split()))) # 1 1 3 7 8
    mlist = list(map(int, sys.stdin.readline().split())) # 1 3 6
    
    start = 0 
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        for i in mlist:
            if nlist[mid] < i:
                start = mid + 1
                answer[testcase] += 1
            else:
                end = mid - 1

    
for testcase in range(t):
    print(answer[testcase])

#아니 ㄹㅇ 뭐함?

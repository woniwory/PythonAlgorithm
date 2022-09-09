t = int(input())
answer = [0] * t

for testcase in range(t):
    
    n, m = map(int, input().split())
    nlist = sorted(list(map(int, input().split()))) # 1 1 3 7 8
    mlist = sorted(list(map(int, input().split()))) # 1 3 6
    start = 0 
    end = n
    while start <= end:
        mid = (start + end) // 2
        for i in nlist:
            for j in mlist:
                if i > j:
                    start = mid + 1
                    answer[testcase] += 1
                else:
                    end = mid - 1
    
    
for testcase in range(t):
    print(answer[testcase])

#아니 ㄹㅇ 뭐함?

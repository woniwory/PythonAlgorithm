import sys



def binary_search(n,nlist,target):    
    start = 0 
    end = n-1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if nlist[mid] > target:
            start = mid + 1
            answer += 1
        else:
            end = mid - 1
    
    print(answer)
    
t = int(input())
for testcase in range(t):
    n, m = map(int, sys.stdin.readline().split())
    nlist = sorted(list(map(int, sys.stdin.readline().split()))) # 1 1 3 7 8
    mlist = sorted(list(map(int, sys.stdin.readline().split()))) # 1 3 6
    for i in mlist:
        binary_search(n,nlist,i)



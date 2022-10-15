n, m = map(int, input().split())

immigration = sorted(list(int(input()) for _ in range(n))) # 알아두기
time = 0


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        
        if mid < target:
            start = mid + 1
        elif mid > target:
            end = mid - 1
            
        
for i in immigration:
 

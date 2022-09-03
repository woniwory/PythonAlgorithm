


n = int(input())
local_list = list(map(int, input().split()))
nation_budget = int(input())

start = 0
end = max(local_list)

    
while start <= end:
    
    mid = (start + end) // 2
    tmp = 0
    
    for local in local_list:
        if local < mid:
            tmp += local
        else:
            tmp += mid
    
    if tmp < nation_budget:
        start = mid + 1
    
    else:
        end = mid - 1 
        
print(end)    

n = int(input())
local_list = list(map(int, input().split()))
nation_budget = int(input()) # 총 예산

start = 1
end = max(local_list)

    
while start <= end:
    
    mid = (start + end) // 2 # 상한액
    tmp = 0 # 배정된 예산의 합
    
    for local in local_list:
        if local < mid:
            tmp += local
        else:
            tmp += mid
    
    if tmp > nation_budget: # tmp < nation_budget으로 작성하면 왜 오답일까 ?
        end = mid - 1 # 예산 상한액은 낮아짐
        
    else:
        start = mid + 1 # 예산 상한액은 높아짐
        
        
print(end)    

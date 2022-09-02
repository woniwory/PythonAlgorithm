

n, k = map(int, input().split())
lan_list = []

for _ in range(n):
    lan_list.append(int(input()))
    
start = 0
end = max(lan_list)
answer = 0

    
while start <= end:
    
    mid = (start + end) // 2
    tmp = 0
 
    for lan in lan_list:
        tmp += lan // mid  
    
    if tmp >= k:
        start = mid + 1
    
    else:
        end = mid - 1 
        
print(end)    

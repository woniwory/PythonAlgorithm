s = int(input())

start = 0
end = s

while start <= end:
    mid = (start + end // 2)
    
    if mid * (mid + 1) // 2 <= s:
        start = mid + 1
        
    else:
        end = mid - 1
        
        
print(mid)        

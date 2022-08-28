# 서로 다른 n 개의 자연수의 합을 s라 할 때 자연수 n의 최댓값은?


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

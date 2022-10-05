x, y = map(int, input().split())


z = y * 100 // x

if z >= 99:
    print(-1)
    
else:
    start = 1
    end = x
    while start <= end:
        mid = (start + end)  // 2
        
        if (y+mid)* 100 // (x+mid) <= z:
            start = mid + 1
        else:
            end = mid - 1
        
    print(mid)        
            
#뭐지 ㅅㅂ?        

n = int(input())
ncard = sorted(list(map(int, input().split())))
#print(ncard)

m = int(input())
mcard = list(map(int, input().split()))
#print(mcard)




for i in range(m):
    status = 0
    start = 0
    end = n-1
    while start <= end:
        
        mid = (start + end) // 2
        
        if mcard[i] > ncard[mid]:
            start = mid + 1

        elif  mcard[i] < ncard[mid]:
            end = mid - 1
 
        else:
            status = 1
            break  
    print(status, end = ' ')
    

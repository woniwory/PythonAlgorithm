n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

#m_list에 있는 수들이 n_list에 존재하는가 ?

start = min(n_list)
end = max(n_list)

def binary_search(start, end, target):    
    while start <= end:
        
        mid = (start + end) // 2 
        
        if mid > target: 
            end = mid - 1 
            
        elif mid < target:
            start = mid + 1 
            
        else:
            return 1
    
    return 0        
 
            

for m in m_list:
    print(binary_search(start, end, m))
    
    
    

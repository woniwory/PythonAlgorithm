n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = sorted(list(map(int, input().split())))
check = [0] * len(m_list)


def binary_search(start, end, target):    
    while start <= end:
        
        mid = (start + end) // 2 
        
        if m_list[mid] > target: 
            end = mid - 1 
            
        elif m_list[mid] < target:
            start = mid + 1 
            
        else:
            return
            
            
for n in n_list:
    binary_search(0, m-1, n)
    
for i in range(len(check)):
    print(check[i], end = ' ')

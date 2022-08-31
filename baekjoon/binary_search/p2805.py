n, m = map(int, input().split())
tree_list = sorted(list(map(int, input().split())))

start = 0
end = max(tree_list)
answer = 0



    
    
while start <= end:
    
    mid = (start + end) // 2
    tmp = 0
 
    for i in tree_list:
        cut_tree = i - mid
        if cut_tree > 0:
            tmp += cut_tree
    
    if tmp >= m:
        start = mid + 1
    
    else:
        end = mid - 1 
        
print(end)

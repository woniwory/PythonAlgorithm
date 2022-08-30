n, m = map(int, input().split())
tree_list = sorted(list(map(int, input().split())))


start = 0
end = len(tree_list)-1 
h = 0

while start < end:
    
    mid = (start + end) // 2
    tmp = 0
    
    for i in range(start, end+1):
        cut_tree = tree_list[i]- tree_list[mid]
        if cut_tree > 0:
            tmp += cut_tree
    
    if tmp > m:
       start = mid + 1
       print(tree_list[mid])
    else:
        end = mid - 1 
        print(tree_list[mid])
    
print(tree_list[mid])

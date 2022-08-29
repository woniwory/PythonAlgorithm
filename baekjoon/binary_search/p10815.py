n = int(input())
ncard = sorted(list(map(int, input().split())))
#print(ncard)

m = int(input())
mcard = sorted(list(map(int, input().split())))
#print(mcard)

start = 0
end = m
mid = 0

def binary_search(start, end, graph, target):
    status = 0
    if target < mid:
        end = mid - 1
    elif target > mid:
        start = mid + 1
    else:
        status = 1
        
    if status == 1:
        print(mid, end = ' ')
        
        
for m data in mcard:
  print(mdata)
  binary_search(start, end, macrd, mdata)

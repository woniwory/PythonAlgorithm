t = int(input())


for _ in range(t):
    
    dp = [0] * 31
    n, m = map(int, input().split())
    
    for n in range(2, n + 1):
        for m in range(2, m + 1):
            
            

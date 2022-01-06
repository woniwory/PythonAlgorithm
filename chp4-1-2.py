n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            tmp = str(i)+str(j)+str(k)
            if '3' in tmp:  #tmp in '3'이 아닌 '3' in tmp라는 점을 기억해두자
                count += 1

print(count)

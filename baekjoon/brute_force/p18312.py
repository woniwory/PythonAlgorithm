n, k = map(int, input().split())
count = 0



for i in range(n+1):
    if i < 10:
        i = '0' + str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        for l in range(60):
            if l < 10:
                l = '0' + str(l)
            tmp = str(i)+str(j)+str(l)
            if str(k) in tmp:
                count += 1


print(count)

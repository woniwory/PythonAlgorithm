n, m = map(int, input().split())
data = list(map(int, input().split()))
tmp = 0

ans = []

for i in data:
    for j in data:
        for k in data:
            if (i != j) and (j != k) and (i != k):
                tmp = i + j + k
                if tmp <= m:
                    ans.append(tmp)

print(max(ans))

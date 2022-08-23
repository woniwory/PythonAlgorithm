n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(min(list(map(int, input().split()))))

data = sorted(data, reverse = True)
print(data[0])


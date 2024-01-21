import sys



n, m = map(int, input().split())
dna_list = ['A', 'C', 'G', 'T']
data = []
ans = []
distance = 0

for _ in range(n):
    data += sys.stdin.readline().split()


for j in range(m):
    tmp = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(n):
            tmp[data[i][j]] += 1
    distance += n - max(tmp.values())
    ans += max(tmp, key=tmp.get)



print(''.join(ans))
print(distance)



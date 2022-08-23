n = int(input())
tmp = 0
res = 0

type = [500, 100,50,10]
for i in type:
    res += n // i
    n = n % i

print(res)

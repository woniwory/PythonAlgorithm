n, m, k = map(int, input().split())
data = list(map(int, input().split()))
res = 0

data = sorted(data, reverse = True)
res =  data[0] * k * (m // k) + data[1] * (m % k)

print(res)


#sort와  sorted의 차이
#얕은 복사와 깊은 복사

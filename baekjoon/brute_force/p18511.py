from itertools import product

n, k = input().split()
max_len = len(n)
data = list(input().split())

while True:
    ans = []

    for i in product(list(data), repeat = max_len):
        tmp = int(''.join(i))
        if tmp <= int(n):
            ans.append(tmp)

    if len(ans) >= 1:
        print(max(ans))
        break

    else:
        max_len -= 1




print(max(ans))

# print(list(product(list(data), repeat = int(k))))
# print(len(list(product(list(data), repeat = int(k)))))
print(max(ans))
# print(len(ans))

from itertools import product

n, k_num = map(int, input().split())
len_max = len(str(n))
k = list(input().split())

while True:
    tmp = list(product(k, repeat=len_max))  # repeat를 통해 몇 개를 뽑을지 결정
    result = []

    for i in tmp:
        if int("".join(i)) <= n:
            result.append(int("".join(i)))

    if len(result) >= 1:
        print(max(result))
        break

    else:
        len_max -= 1

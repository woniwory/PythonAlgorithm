n = int(input())
subtotal = 0
ans = 0
# n = subtotal + m

for i in range(1, n+1):
    subtotal = sum(map(int, str(i)))
    ans = i + subtotal
    if ans == n:
        print(i)
        break
    if i == n:
        print(0)



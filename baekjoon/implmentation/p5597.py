submit = []
check = [False] * 31

for _ in range(28):
    tmp = int(input())
    submit.append(tmp)
    check[tmp-1] = True

for i in range(len(check)-1):
    if check[i] == False:
        print(i+1)

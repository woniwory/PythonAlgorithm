a,b,c,m = map(int, input().split())
ans = 0
fatigue = 0

for _ in range(24):
    if fatigue + a <= m:
        ans += b
        fatigue += a
    else:
        fatigue -= c
        if fatigue - c < 0:
            fatigue = 0



print(ans)

# 하루에 한 시간 일하면 피로도는 5(A)만큼 쌓이고 일은 3(B)만큼 처리할 수 있다
# 한 시간을 쉰다면 피로도는 2(C)만큼 줄어든다
# 피로도 >= 0이다.
# 피로도 M을 넘지 않게 일을 하려고 한다.
# 하루는 24시간이다.
# 최대 얼마나 일을 할 수 있을까

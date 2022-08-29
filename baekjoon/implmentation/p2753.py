year = int(input())

# 연도가 4의 배수이면서(1), 100의 배수가 아닐 때(2) 또는 400의 배수일 때이다(3) : (1)인 상태에서 (2) or (3)이어야한다.

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(1)
else:
    print(0)

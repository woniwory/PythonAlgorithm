a, b, c, d, e, f = map(int, input().split())


for x in range(-999, 1000):
    y = (c - f - (a-d) * x) / (b-e)
    if (a+d) * x + (b+e) * y == c + f:
        print(x, int(y))
        break





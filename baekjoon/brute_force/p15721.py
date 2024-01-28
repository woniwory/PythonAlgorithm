a = int(input())
t = int(input())
p = input()
tmp = {'0': 0, '1': 0}
round_count = 1
person_count = 0
threshold = 0


student = [i for i in range(a)]
game = []



while True:
    game = '0101' + '0' * (round_count+1) + '1' * (round_count+1) # +=으로 쓰니까 오류가 나지..
    # print(game)

    for i in game:
        if i == '0':
            tmp['0'] += 1
            person_count += 1
            if t == tmp.get(p):
                threshold = 1
                break
        else:
            tmp['1'] += 1
            person_count += 1
            if t == tmp.get(p):
                threshold = 1
                break
        # print(tmp, person_count)

    round_count += 1
    if threshold == 1:
        print(student[(person_count%a)-1])
        break

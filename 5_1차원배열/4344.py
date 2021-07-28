# 평균운 넘겠지

c = int(input())

for _ in range(c):
    test = list(map(int, input().split()))
    avg = sum(test[1:]) / test[0]
    cnt = 0
    for x in test[1:]:
        if x > avg:
            cnt += 1
    answer = cnt / test[0] * 100
    print(f'{answer:.3f}%')

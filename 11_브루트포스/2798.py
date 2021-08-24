# 블랙잭
from itertools import combinations

n, m = map(int, input().split())

black_jack = []

cards = list(map(int, input().split()))

for tmp_list in list(combinations(cards, 3)):
    tmp = sum(tmp_list)
    if tmp <= m:
        black_jack.append(tmp)

print(max(black_jack))

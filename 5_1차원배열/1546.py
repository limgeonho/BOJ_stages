# 평균

n = int(input())
res = list(map(int, input().split()))
high_res = max(res)

change = []
for x in res:
    change.append(x/high_res*100)

print(sum(change)/len(change))

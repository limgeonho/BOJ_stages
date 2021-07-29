# 그룸 단어 체커

n = int(input())

cnt = 0
for _ in range(n):
    s = input()
    check = []
    for char in s:
        if not check:
            check.append(char)
        else:
            if check[-1] == char:
                check.append(char)
            else:
                if char in check:
                    cnt += 1
                    break
                else:
                    check.append(char)
print(n - cnt)

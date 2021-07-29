# 단어 공부

s = input()

small = s.lower()

check = {}

cnt = 0
tmp = ''
for char in small:
    check[char] = check.get(char, 0) + 1

num = max(check.values())

for k, v in check.items():
    if v == num:
        cnt += 1
        tmp = k
if cnt > 1:
    print('?')
else:
    print(tmp.upper())

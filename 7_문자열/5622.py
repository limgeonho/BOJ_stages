# 다이얼

s = input()

phone = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL',
         6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}

cnt = 0
for char in s:
    for k, v in phone.items():
        if char in v:
            cnt += k+1

print(cnt)

# li = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# word = input()
# cnt = 0
# for char in word:
#     for letter in li:
#         if char in letter:
#             cnt += li.index(letter) + 3
# print(cnt)

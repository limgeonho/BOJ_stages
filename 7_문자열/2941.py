# 크로아티아 알파벳

s = input()
c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in c_alpha:
    s = s.replace(char, '0')

print(len(s))

# s = s.replace(char, '0') => replace한 문자열s를 다시 s에 넣고 또다시 바뀐 s로 다시 돌림

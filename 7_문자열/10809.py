# 알파벳 찾기

s = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for char in alphabet:
    if char in s:
        print(s.index(char), end=' ')
    else:
        print(-1, end=' ')

# 아.. find() 가 더 좋네요...

# 상수

a, b = input().split()

# if int(a[::-1]) > int(b[::-1]):
#     print(a[::-1])
# else:
#     print(b[::-1])

print(max(int(a[::-1]), int(b[::-1])))

# 소트인사이드

# num = int(input())
# tmp = []

# while num > 0:
#     tmp.append(str(num % 10))
#     num = num // 10
# tmp.sort(reverse=True)
# answer = ''.join(tmp)
# print(answer)

num2 = input()
print(''.join(sorted(num2)[::-1]))

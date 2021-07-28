# O, X 퀴즈

t = int(input())

for _ in range(t):
    score = 0
    check = 1
    answer = 0
    quiz = input()
    for x in quiz:
        if x == 'O':
            answer += check
            check += 1
        else:
            check = 1
    print(answer)

# 스위치 켜고 끄기

n = int(input())
switches = [0] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())
    if gender == 1:
        cnt = 1
        while True:
            tmp = num * cnt
            if tmp > n:
                break
            else:

                if switches[tmp] == 1:
                    switches[tmp] = 0
                else:
                    switches[tmp] = 1
                cnt += 1
    else:
        changed_idx_f = changed_idx_b = num
        flag = False
        while True:
            changed_idx_f -= 1
            changed_idx_b += 1
            if changed_idx_f == 0 or changed_idx_b == n+1 or flag:
                break

            if switches[changed_idx_f] == switches[changed_idx_b]:
                if switches[changed_idx_b] == 1:
                    switches[changed_idx_b] = 0
                    switches[changed_idx_f] = 0
                else:
                    switches[changed_idx_b] = 1
                    switches[changed_idx_f] = 1
            else:
                flag = True
        if switches[num] == 1:
            switches[num] = 0
        else:
            switches[num] = 1
answer = switches[1:]

cnt_2 = 0

for i in range(len(answer)):
    print(answer[i], end=' ')
    cnt_2 += 1
    if cnt_2 % 20 == 0:
        print()
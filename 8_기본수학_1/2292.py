# 벌집

n = int(input())

a = 1
plus = 6
room = 1
if n == 1:
    print(1)
else:
    while True:
        a = a + plus
        room += 1
        if n <= a:
            print(room)
            break
        plus += 6

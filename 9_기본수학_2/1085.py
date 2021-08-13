# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

row = min(w-x, x-0)
col = min(h-y, y-0)

print(min(row, col))

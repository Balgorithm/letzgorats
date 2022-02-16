import sys
input = sys.stdin.readline

current = input().strip()
row = int(current[1])-1 # 1부터 시작하니까 0으로 맞추기위해
col = ord(current[0])-97 # a부터 시작하니까 0으로 맞추기 위해

# 나이트가 움직일 수 있는 방향 8가지
knight_move = [(-2,-1),(-2,1),(-1,-2),(1,-2),(-1,2),(1,2),(2,-1),(2,1)]

count = 0 
for cmd in knight_move: # 8방향으로 움직이는 좌표를 차례로
    nr = row + cmd[0] # 현재 행에 적용
    nc = col + cmd[1] # 현재 열에 적용
    if 0 <= nr < 8 and 0 <= nc < 8 :  # 범위 안쪽이면
        count += 1  # count 1 증가
print(count)

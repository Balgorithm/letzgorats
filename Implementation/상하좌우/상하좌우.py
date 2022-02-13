import sys
input = sys.stdin.readline

n = int(input())  # 공간의 크기를 나타내는 n을 입력받기
plan = list(input().split())  # 이동할 계획서의 내용이 주어진다.
dr = [0,0,-1,1] # L R U D 순서(행)
dc = [-1,1,0,0] # L R U D 순서(열)

nowr,nr = 0,0 # 현재의 행을 0이라고 가정( 문제에서는 (0,0)을 (1,1)이라고 가정했으니 마지막에만 1을 더해주면 된다.)
nowc,nc = 0,0 # 현재의 열을 0이라고 가정
graph = [[0]*n for _ in range(n)] # graph_visit을 쓰려고 임시로 만들어놓은 graph - 여기서는 활용 안함
graph[0][0] = 1 # 현재 (0,0)은 방문  - 여기서는 활용 안함

for cmd in plan:  # plan에 들어있는 cmd를 차례로 보면서
  if cmd == "L":
        nc = nowc + dc[0] # L이면 왼쪽으로 가므로 열-1
        if 0 <= nc < n :  # 범위 안쪽이라면
            nowc = nc   # 이동
    elif cmd == "R":  
        nc = nowc + dc[1] # R이면 오른쪽으로 가므로 열+1
        if 0 <= nc < n :  # 범위 안쪽이라면
            nowc = nc   # 이동
    elif cmd == "U":  
        nr = nowr + dr[2] # U면 위쪽으로 가므로 행-1
        if 0 <= nr < n :  # 범위 안쪽이라면
            nowr = nr # 이동
    elif cmd == "D":  
        nr = nowr + dr[3] # D면 아래쪽으로 가므로 행+1
        if 0 <= nr < n :  # 범위 안쪽이라면
            nowr = nr # 이동 

print(nr+1,nc+1)

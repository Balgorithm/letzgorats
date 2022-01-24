import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # n,m 입력받기
ball_list = list(map(int,input().split()))  # 볼링골 무게 리스트 입력받기
count = 0 # count 0으로 초기화
idx = 0 # idx 0부터 시작
for a in ball_list[idx:]: # a는 0부터
    for b in ball_list[idx+1:]: # b는 1부터
        if a!=b :
            count += 1
    idx += 1  # b 다돌면 idx 1증가
print(count)

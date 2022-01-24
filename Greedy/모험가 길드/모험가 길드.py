import sys
input = sys.stdin.readline

n = int(input()) # n 입력받기
fear_list = sorted(list(map(int,input().split()))) # fear_list 정렬
group = 0 
idx = 0 # 초기 idx(처음 idx) 0으로 설정
while idx != n: # idx가 fear_list 인덱스 끝까지 갈 때까지
    if idx + fear_list[idx] >= n:   # idx 범위 예외처리
        if fear_list[idx] == 1: # fear_list[idx] 값이 1 이면 
            group += 1  # 현재 가리키는 그 값도 더해줘야 한다.
        break
    group += 1 # if 문에 안 걸리면 group 1 증가  
    idx +=  fear_list[idx] # 현재 가리키는 fear_list[idx] 만큼 idx 증가
print(group)

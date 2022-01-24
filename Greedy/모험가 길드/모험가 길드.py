import sys
input = sys.stdin.readline

n = int(input())  # n 입력받기 
fear_list = sorted(list(map(int,input().split())))  # fear_list 정렬
group = 0
# 1 2 2 2 3
idx = 0 # 초기 idx(처음 idx) 0으로 설정
while idx != n : # idx가 fear_list 인데스 끝까지 갈 때까지  
    if idx > n or idx + fear_list[idx] > n : # idx 범위 예외처리
        break
    group += 1 # group 1증가 
    idx +=  fear_list[idx]  # 현재 가리키는 fear_list[idx] 만큼 idx를 증가
print(group) 

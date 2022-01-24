import sys
input = sys.stdin.readline

n = int(input()) # n 입력받기
fear_list = sorted(list(map(int,input().split()))) # fear_list 정렬
group = 0 
idx = 0 # 초기 idx(처음 idx) 0으로 설정
temp = 0 
while idx != n: # idx가 fear_list 인덱스 끝까지 갈 때까지
    temp += 1
    if (temp >= fear_list[idx]):
        temp = 0
        group += 1
    idx += 1 
print(group)

# 답지 풀이
import sys
input = sys.stdin.readline

n = int(input()) # n 입력받기
fear_list = sorted(list(map(int,input().split()))) # fear_list 정렬
temp = 0 # 사람 수 
group = 0 
idx = 0 # 초기 idx(처음 idx) 0으로 설정
for fear in fear_list:
    temp += 1 # 사람 수 1 증가 
    if temp >= fear: # 사람 수가 해당 공포도와 같아지는 순간 
        group += 1 # 그룹수 1 증가 
        temp = 0  # 사람 수 0으로 다시 초기화

print(group)

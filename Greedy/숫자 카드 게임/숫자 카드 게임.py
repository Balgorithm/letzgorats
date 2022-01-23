import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # n행 m열
answer = 1 # 각 숫자는 1이상 10000이하의 자연수이므로 일단 최소값 1로 설정
for _ in range(n): # n행 반복
    n_list = list(map(int,input().split())) # 각 행마다 숫자 입력받기
    answer = max(answer,min(n_list)) # answer은 기존의 answer과 해당 행에서 가장 작은 값 중 큰 값을 골라냄
print(answer)
